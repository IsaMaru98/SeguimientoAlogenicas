from ninja import NinjaAPI, Schema, Router
import httpx 

router = Router() 

api = NinjaAPI()

class HelloSchema(Schema):
    name: str = "potato"

@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}"

# @api.get("/hello")
# def hello(request, name: str ="mundo"):
#     return f"Hola {name}"

# @api.get("/math")
# def math(request, a: int, b: int):
#     return {"add": a + b, "multiply": a * b}

#Ahora defino los parametros con la misma sintaxis que al fomatear strings  localhost:8000/api/math/2and3

@api.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    # Unauthenticated users don't have the following fields, so provide defaults.
    email: str 
    first_name: str 
    last_name: str 
class Error(Schema): 
    message: str 

@api.get("/me", response={200: UserSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user 

# @router.get("/data")
# def fetch_and_transform(request):
#     url = "https://cellslife.co/crm/solicitudServicio"  # Replace with the URL of the external website's API or data source
    
    
#     # Send an HTTP GET request to fetch data from the external website
#     response = httpx.get(url)
#     if response.status_code == 200:
#         data = response.json()  # Assuming the response is in JSON format

#         # Perform any necessary data manipulation or transformation here
#         #transformed_data = transform_data(data)
#         print("datos recuperados")
#     else:
#         return {"error": "Failed to fetch data from the external website"}
