export async function onRequestGet() {
  return new Response(JSON.stringify({
    status: 'ok',
    mode: 'cloudflare-pages-functions',
    message: 'Dynamic API is ready for Cloudflare Pages.',
    timestamp: new Date().toISOString()
  }), {
    headers: {
      'content-type': 'application/json; charset=utf-8'
    }
  });
}
