from django.shortcuts import render

# +MowKeoJK38z7AwPV2obcQ==KJ51izUz5GscMfPE
# Create your views here.
def index(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        apiUrl = 'https://api.api-ninjas.com/v1/nutrition?query='
        apiRequest = requests.get(apiUrl + query, headers={'X-Api-Key': '+MowKeoJK38z7AwPV2obcQ==KJ51izUz5GscMfPE'})
        try:
            data = json.loads(apiRequest.content)
            print(apiRequest.content)
        except Exception as e:
            data = "Sorry, there was an error!"
            print(e)
        return render(request, 'index.html', {'data': data})
    else:
        return render(request, 'index.html',{'query': 'Put a valid query'})
    
