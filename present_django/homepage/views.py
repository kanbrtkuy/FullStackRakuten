# from django.shortcuts import render
# from django.http import JsonResponse
# # Create your views here.
# from django.views.generic import FormView
# from .models import Search
# from .forms import SearchForm
# import json
# import requests
#
# SEARCH_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'
# api_key = '1082911034148481341'
#
#
#
#
# def get_api_data(params):
#     api = requests.get(SEARCH_URL, params=params).text
#     result = json.loads(api)
#     items = result["Items"]
#     return items
#
#
# class IndexView(FormView):
#     # model = Search
#     template_name = "myapp/index.html"
#     form_class = SearchForm
#
#     def form_valid(self, form):
#         keyword = form.cleaned_data['title']
#         params = {
#             'applicationId': api_key,
#             'keyword': keyword,
#             'sort': '+updateTimestamp',
#         }
#         items = get_api_data(params)
#         item_data = []
#         for i in items:
#             item = i['Item']
#             itemPrice = item['itemPrice']
#             itemName = item['itemName']
#             image = item['mediumImageUrls'][0]['imageUrl']
#             query = {
#                 'title': itemName,
#                 'price': itemPrice,
#                 'image': image,
#             }
#             item_data.append(query)
#
#         return render(self.request, 'myapp/result.html', {
#             'item_data': item_data,
#             'keyword': keyword
#         })

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import FormView
from .models import Search
from .forms import SearchForm
import json
import requests

SEARCH_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'
api_key = '1082911034148481341'

def get_api_data(params):
    api = requests.get(SEARCH_URL, params=params).text
    result = json.loads(api)
    items = result["Items"]
    return items

class IndexView(FormView):
    template_name = "myapp/index.html"
    form_class = SearchForm

    def form_valid(self, form):
        keyword = form.cleaned_data['title']
        sort = self.request.POST.get('sort', 'standard')  # 获取排序参数，默认为standard
        params = {
            'applicationId': api_key,
            'keyword': keyword,
            'sort': sort,
        }
        items = get_api_data(params)
        item_data = []
        for i in items:
            item = i['Item']
            itemPrice = item['itemPrice']
            itemName = item['itemName']
            image = item['mediumImageUrls'][0]['imageUrl']
            query = {
                'title': itemName,
                'price': itemPrice,
                'image': image,
            }
            item_data.append(query)

        return render(self.request, 'myapp/result.html', {
            'item_data': item_data,
            'keyword': keyword
        })
