import os
from datetime import datetime
from django.shortcuts import render
import plotly.express as px
from minio import Minio

from core.forms import PoolForm

MINIO_ENDPOINT = os.environ["MINIO_ENDPOINT"]
ACCESS_KEY = os.environ["ACCESS_KEY"]
SECRET_KEY = os.environ["SECRET_KEY"]

# Create your views here.
def chart(request):
    network = request.GET.get('network')
    token0 = request.GET.get('token0')
    token1 = request.GET.get('token1')

    if network is None:
        network = "bsc"
    if token0 is None:
        token0 = "USDT"
    if token1 is None:
        token1 = "MAV"

    _client = Minio(
        MINIO_ENDPOINT,
        secure=False,
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY,
    )
    pool_data = _client.get_object(network, f"{token0}_{token1}.json").json()


    fig = px.bar(
        x=[datetime.fromtimestamp(pool_record["date"]) for pool_record in pool_data],
        y=[float(pool_record["feesUSD"]) for pool_record in pool_data],
        title=f"({network}) {token0}_{token1}",
        labels={'x': 'Date', 'y': 'feesUSD'}
    )
    fig.update_layout(
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
    })
    feesUSD = fig.to_html()


    fig = px.bar(
        x=[datetime.fromtimestamp(pool_record["date"]) for pool_record in pool_data],
        y=[float(pool_record["tvlUSD"]) for pool_record in pool_data],
        labels={'x': 'Date', 'y': 'tvlUSD'}
    )
    fig.update_layout(
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
        })
    tvlUSD = fig.to_html()


    context = {'feesUSD': feesUSD, 'tvlUSD': tvlUSD, 'form': PoolForm()}
    return render(request, 'core/chart.html', context)
