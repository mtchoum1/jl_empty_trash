from typing import Optional

from jupyter_server.serverapp import ServerApp
from prometheus_client import Gauge

from jl_empty_trash.metrics import TrashMetricsLoader

try:
    from traitlets import Callable
except ImportError:
    from .utils import Callable

class PrometheusHandler(Callable):
    def __init__(self, metrics_loader: TrashMetricsLoader):
        super().__init__()
        self.metrics_loader = metrics_loader
        self.config = metrics_loader.config
        self.session = metrics_loader.jsapp.session_manager

        gauge_name = ["total_home", "max_home"]
        for name in gauge_name:
            phrase = name + "_usage"
            gauge = Gauge(phrase, "counter for " + phrase.replace("_", " "), [])
            setattr(self, phrase.upper(), gauge)

    async def __call__(self, *args, **kwargs):
        disk_metric_values = self.metrics_loader.disk_metrics()
        self.TOTAL_HOME_USAGE.set(disk_metric_values["disk_usage"])
        self.MAX_HOME_USAGE.set(self.apply_disk_limit(disk_metric_values))

    def apply_disk_limit(self, disk_metric_values: dict) -> Optional[int]:
        if disk_metric_values is None:
            return None
        else:
            if callable(self.config.disk_limit):
                return self.config.disk_limit(disk_usage=disk_metric_values["disk_usage"])
            elif self.config.disk_limit > 0:
                return self.config.disk_limit
            else:
                return disk_metric_values["disk_total"]