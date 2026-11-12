// Serve only the built Pages artifact, with its production base path and 404.
const http = require('node:http');
const fs = require('node:fs/promises');
const path = require('node:path');
const root = path.resolve(__dirname, '../_site');
const port = Number(process.env.PORT || 8768);
const types = { '.html':'text/html; charset=utf-8', '.css':'text/css', '.js':'text/javascript', '.svg':'image/svg+xml', '.png':'image/png', '.json':'application/json', '.xml':'application/xml', '.txt':'text/plain', '.md':'text/plain; charset=utf-8' };
http.createServer(async (request,response) => {
  try {
    const url = new URL(request.url, `http://127.0.0.1:${port}`);
    if (url.pathname === '/') { response.writeHead(302,{Location:'/Project-Lux/'}); response.end(); return; }
    let relative = decodeURIComponent(url.pathname);
    if (!relative.startsWith('/Project-Lux/')) throw new Error('outside base');
    relative = relative.slice('/Project-Lux/'.length);
    if (!relative || relative.endsWith('/')) relative += 'index.html';
    const filename = path.resolve(root, relative);
    if (!filename.startsWith(root + path.sep)) throw new Error('outside artifact');
    const body = await fs.readFile(filename);
    response.writeHead(200, {'Content-Type':types[path.extname(filename)] || 'application/octet-stream','Cache-Control':'no-store'});
    response.end(request.method === 'HEAD' ? undefined : body);
  } catch {
    response.writeHead(404, {'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-store'});
    response.end(await fs.readFile(path.join(root, '404.html')));
  }
}).listen(port,'127.0.0.1',()=>console.log(`Project Lux preview: http://127.0.0.1:${port}/Project-Lux/`));
