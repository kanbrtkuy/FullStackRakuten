from django.shortcuts import render

# Create your views here.

import requests
from django.http import JsonResponse


def rakuten_api(request):
    api_key = '1082911034148481341'
    base_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'

    # 定义查询参数
    params = {
        'applicationId': api_key,
        'keyword': 'お土産',
        'format': 'json',  # The response format can be json or xml, json is selected here
    }

    try:
        # Send a GET request to the Rakuten Ichiba API
        response = requests.get(base_url, params=params)

        # check response status code
        if response.status_code == 200:
            # Return the API response as JSON to the client
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'API request failed'}, status=response.status_code)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
