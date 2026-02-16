from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.userregister_routes import router as user_router
from server.routes.login_routes import router as login_router
from server.routes.contact_route import router as contact_router
from server.routes.email_routes import router as email_router
from server.routes.otp_routes import router as otp_router
from server.routes.common_router import router as common_router
from server.routes.allforms_router import router as all_form_router
from server.routes.resetpassword_router import router as forget_password_router
from server.routes.individual_user_get_router import router as individual_users_router
from server.routes.organization_user_get_router import router as organization_users_router
app = FastAPI(title="User Registration API")


origins = [
    "http://localhost:4004",
    "http://127.0.0.1:4004",

]
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
     allow_origins=["*"],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(user_router)
app.include_router(login_router)
app.include_router(contact_router)
app.include_router(email_router)
app.include_router(otp_router)
app.include_router(common_router)
app.include_router(all_form_router)
app.include_router(forget_password_router)
app.include_router(individual_users_router)
app.include_router(organization_users_router)
@app.get("/")
async def root():
    return {"message": "API Running"}
