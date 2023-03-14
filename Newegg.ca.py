import requests
import pandas as pd
from pprint import pprint

data = []
iteam_id = []
name = []
title = []
short_title = []
manual_product_name = []
review = []
no_review = []
unit_cost = []
price = []
discount = []
offer_date = []

for i in range(1,110):
    params = (
            ('pageIndex', str(i)),
             ('pageSize', '60'),
              ('enableSpaItem', 'true'),
        )
    response = requests.get('https://www.newegg.ca/store/api/GetShopAllDeals', params=params)
    json_data = response.json()
    # print(json_data)
    keys = json_data.keys()
    # print(keys)
    iteam_list_data = json_data['ItemList']
    # print(iteam_list_data)

    """
    iteam_id = iteam_list_data[0]['ItemGroupID']
    name = iteam_list_data[0]['Description']['ProductName']
    title = iteam_list_data[0]['Description']['Title']
    short_title = iteam_list_data[0]['Description']['ShortTitle']
    manual_product_name = iteam_list_data[0]['Description']['ManualProductName']
    rating = iteam_list_data[0]['Review']['Rating']
    human_rating = iteam_list_data[0]['Review']['HumanRating']
    unit_cost = iteam_list_data[0]['UnitCost']
    price = iteam_list_data[0]['FinalPrice']
    discount = iteam_list_data[0]['InstantRebateAmount']
    offer_date = iteam_list_data[0]['SaleEndTimeText']
    # print(offer_date)
    """

    for iteam in iteam_list_data:

        iteam_id = iteam['ItemGroupID']
        name = iteam['Description']['ProductName']
        title = iteam['Description']['Title']
        short_title = iteam['Description']['ShortTitle']
        manual_product_name = iteam['Description']['ManualProductName']
        review = iteam['Review']['Rating']
        no_review = iteam['Review']['HumanRating']
        unit_cost = iteam['UnitCost']
        price = iteam['FinalPrice']
        discount = iteam['InstantRebateAmount']
        offer_date = iteam['SaleEndTimeText']

        iteams = {
            'iteam_id': iteam_id,
            'name': name,
            'title': title,
            'short_title': short_title,
            'manual_product_name': manual_product_name,
            'review': review,
            'no_review': no_review,
            'unit_cost': unit_cost,
            'price': price,
            'discount': discount,
            'offer_date': offer_date

        }
        data.append(iteams)

    product_data = pd.DataFrame(data)
    product_data.to_csv('newegg.csv', index=False)



