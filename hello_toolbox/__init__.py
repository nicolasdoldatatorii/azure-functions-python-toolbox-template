import logging

import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except:
        return func.HttpResponse("Request does not contain a json")
        
    if not "sharepoint_url" in req_body:
        return func.HttpResponse(
            json.dumps({
                "status": "Error",
                "message": "No URL in body"
            }),status_code=400
        )

    return func.HttpResponse(req_body["sharepoint_url"])
