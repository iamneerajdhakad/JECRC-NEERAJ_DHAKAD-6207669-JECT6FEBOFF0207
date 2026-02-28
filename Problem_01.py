# E-Commerce Order Revenue Analyzer

class Solution:

    def city_revenue(self, orders):
        revenue_dict = {}
        ## Write your code here and don't forget to return value.
        max = float('-inf')
        str=''
        result = []
        for element in orders:
            if element['city'] not in revenue_dict:
                revenue_dict[element['city']]=element['amount']
            else:
                revenue_dict[element['city']]+= element['amount']
        
        for key,val in revenue_dict.items():
            if(max<revenue_dict[key]):
                max=val
                str=key
        result.append(revenue_dict)
        result.append(str)

        return result
