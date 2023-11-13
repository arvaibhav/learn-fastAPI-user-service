import time
from fastapi import Request, HTTPException
import random
import logging.config
from fastapi.responses import JSONResponse
import traceback

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


async def logging_middleware(request: Request, call_next):
    request_id = random.randint(0, 10000)
    request_start_time = time.time()
    server_error = None
    request_body = await request.body()
    try:
        response = await call_next(request)
    except HTTPException as error_response:
        response = error_response
    except:
        server_error = traceback.format_exc()
        response = JSONResponse(status_code=500, content={"internalServerError": True})

    request_end_time = time.time()

    # Collect request and response information
    response.headers["X-Request-ID"] = str(request_id)
    log_data = {
        "asctime": time.strftime(
            "%Y-%m-%d %H:%M:%S", time.gmtime()
        ),  # Request time (UTC)
        "name": __name__,  # Logger name
        "levelname": "INFO",  # Log level (assuming INFO for middleware)
        "message": f"rid={request_id} completed_in={request_end_time - request_start_time:.3f}s",
        "request_time": request_end_time,  # Request end time (Linux way)
        "request_id": request_id,  # Request ID
        "request_method": request.method,  # Request method
        "request_header": dict(request.headers),  # Request headers
        "request_meta": {
            "path": request.url.path,
            "query_params": dict(request.query_params),
            "client": request.client,
            "request_body": request_body,
        },
        "response_body": response._info,  # Response body
        "response_header": dict(response._headers),  # Response headers
        "response_http_code": response.status_code,  # Response HTTP code
        "server_error": server_error,
    }
    severity = "info"
    if server_error:
        severity = "error"
    getattr(logger, severity)(log_data)
    return response


"""
"log shipping" or "log forwarding." This approach involves collecting logs locally on each application server 
(A, B, C), storing them in log files or a local log storage system, and then periodically shipping or 
forwarding those logs to a centralized log server (Z) in the background.

Log SHIPPING AGENTS
Filebeat (for ELK Stack Integration):

Reliability: Filebeat, developed by Elastic, is known for its reliability and efficiency in log shipping.
 It's a lightweight log shipper designed to send log data to various destinations, including Elasticsearch, 
 Logstash, or other central log servers.
Adoption: Filebeat is highly adopted in the industry, particularly in organizations that use the ELK Stack
 (Elasticsearch, Logstash, Kibana) for log management and visualization.
Integration: It seamlessly integrates with Elasticsearch and can be used to ship logs to Grafana Loki when 
configured properly. Filebeat can also handle log rotation and ensure logs are shipped reliably.
Fluentd:

Reliability: Fluentd is another reliable log shipping tool that is popular for log aggregation and forwarding.
 It is known for its robustness and flexibility in handling various log sources and formats.
Adoption: Fluentd has gained significant adoption, especially in environments with diverse log sources and 
complex log processing requirements. It has a broad user base and active community support.
Integration: Fluentd can collect logs from various sources, including log files, and forward them to different
 destinations, making it adaptable to your log storage and visualization needs. 
 Fluentd can be configured to send logs to Grafana Loki, among other destinations.

LOG AGGREGATOR
GRAFANA LOKI
ELASTIC SEARCH LOGSTASH

"""
