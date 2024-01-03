from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    html_content = """
    <html>
        <body>
            <h1>Welcome to Animerobots</h1>
            <img src="Base/PFPZ/WPnone.jpg" alt="Your Image">
        </body>
    </html>
    """
    return web.Response(text=html_content, content_type="text/html")
    #return web.json_response("Animerobots")
