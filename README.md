# LittleLemon

Little Lemon Reservation API

## Superuser credentials

- **Username:** admin
- **Password:** adminadmin

## API Endpoints

### Home

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | Home page (index.html) |

### Menu

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/restaurant/menu/` | List all menu items |
| POST | `/restaurant/menu/` | Create a menu item |
| GET | `/restaurant/menu/<id>/` | Retrieve a single menu item |
| PUT | `/restaurant/menu/<id>/` | Update a menu item |
| PATCH | `/restaurant/menu/<id>/` | Partially update a menu item |
| DELETE | `/restaurant/menu/<id>/` | Delete a menu item |

### Booking (requires authentication)

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/restaurant/booking/tables/` | List all bookings |
| POST | `/restaurant/booking/tables/` | Create a booking |
| GET | `/restaurant/booking/tables/<id>/` | Retrieve a single booking |
| PUT | `/restaurant/booking/tables/<id>/` | Update a booking |
| PATCH | `/restaurant/booking/tables/<id>/` | Partially update a booking |
| DELETE | `/restaurant/booking/tables/<id>/` | Delete a booking |

### Authentication

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/restaurant/api-token-auth/` | Obtain auth token |
| POST | `/auth/token/login/` | Djoser token login |
| POST | `/auth/token/logout/` | Djoser token logout |
| GET | `/auth/users/` | List users |
| POST | `/auth/users/` | Register a new user |

### Admin

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/admin/` | Django admin panel |
