"""Checks for types belonging to the pynwb.behavior module."""
from pynwb.behavior import SpatialSeries

from ..register_checks import register_check, Importance, InspectorMessage


@register_check(importance=Importance.CRITICAL, neurodata_type=SpatialSeries)
def check_spatial_series_dims(spatial_series: SpatialSeries):
    """Check if a SpatialSeries has the correct dimensions."""
    if len(spatial_series.data.shape) > 1 and spatial_series.data.shape[1] > 3:
        return InspectorMessage(
            message="SpatialSeries should have 1 column (x), 2 columns (x, y), or 3 columns (x, y, z)."
        )