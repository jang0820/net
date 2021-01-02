from django import forms
IP_items = [("203.68.236."+str(ip), "203.68.236."+str(ip)) for ip in range(1,255)]
class SearchIPForm(forms.Form):
    ip = forms.CharField(max_length=50)

class SearchIPSelectForm(forms.Form):
    ip = forms.CharField(label='請選擇IP?', widget=forms.Select(choices=IP_items))

class SearchIPRangeForm(forms.Form):
    ip1 = forms.CharField(max_length=20)
    ip2 = forms.CharField(max_length=20)