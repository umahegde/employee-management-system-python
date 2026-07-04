import logging

logging.basicConfig(
    filename="log/employee.log",
    level=logging.INFO
)

logger = logging.getLogger(__name__)