// AI Pulse — service worker v2 (network-first for HTML, cache for assets)
const CACHE = 'ai-pulse-v2';
const ASSETS = ['./manifest.json', './assets/favicon.svg'];

// Install: only cache static assets, never the page itself
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

// Fetch: network-first for HTML, cache-first for static assets
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  // HTML pages: always go network first, no cache
  if (e.request.destination === 'document' || url.pathname.endsWith('.html')) {
    e.respondWith(
      fetch(e.request).catch(() => caches.match(e.request))
    );
    return;
  }
  // Static assets: cache-first
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request).then(res => {
      if (res.ok && res.type === 'basic') {
        const clone = res.clone();
        caches.open(CACHE).then(c => c.put(e.request, clone));
      }
      return res;
    }))
  );
});

// Activate: purge old caches
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
  ));
  self.clients.claim();
});
