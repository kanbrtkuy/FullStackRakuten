from django.shortcuts import render

# Create your views here.

import requests
from django.http import JsonResponse
import requests
import json
from django.shortcuts import render


def rakuten_api(request):
    api_key = '1082911034148481341'
    base_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'
    keyword = request.GET.get('keyword', 'お土産')
    sort = request.GET.get('sort', 'standard')  # 获取排序方式，默认为standard

    # 定义查询参数
    params = {
        'applicationId': api_key,
        'keyword': keyword,
        'format': 'json',
        'sort': sort,  # 将用户选择的排序方式传递给API请求
    }

    try:
        # Send a GET request to the Rakuten Ichiba API
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            items = [{'name': item['Item']['itemName'], 'price': item['Item']['itemPrice']} for item in data['Items']]
            return render(request, 'myapp/rakuten_api.html', {'items': items})

        else:
            return JsonResponse({'error': 'API request failed'}, status=response.status_code)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

