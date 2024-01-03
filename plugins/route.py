from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    with open("WebPage.html", "r") as file:
        html_content = file.read()
    return web.Response(text=html_content, content_type="text/html")
    #return web.json_response("Animerobots")
