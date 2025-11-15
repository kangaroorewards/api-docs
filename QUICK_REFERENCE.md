# Kangaroo Rewards API Quick Reference

A quick reference guide for the most common API operations.

## Authentication

### Get Access Token (Password Grant)

```bash
curl -X POST https://api.kangaroorewards.com/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-Application-Key: YOUR_APP_KEY" \
  -d "grant_type=password" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "username=user@example.com" \
  -d "password=USER_PASSWORD" \
  -d "scope=admin" \
  -d "application_key=BUSINESS_APP_KEY"
```

### Refresh Access Token

```bash
curl -X POST https://api.kangaroorewards.com/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-Application-Key: YOUR_APP_KEY" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=YOUR_REFRESH_TOKEN" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "scope=admin"
```

## Customers

### List Customers

```bash
GET https://api.kangaroorewards.com/customers
Headers:
  Authorization: Bearer ACCESS_TOKEN
  X-Application-Key: YOUR_APP_KEY
  Accept: application/vnd.kangaroorewards.api.v1+json
```

### Get Customer by ID

```bash
GET https://api.kangaroorewards.com/customers/{customer_id}
```

### Create Customer

```bash
POST https://api.kangaroorewards.com/customers
Body:
{
  "email": "customer@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "phone": "5551234567",
  "country_code": "US"
}
```

### Update Customer

```bash
PUT https://api.kangaroorewards.com/customers/{customer_id}
Body:
{
  "first_name": "Jane",
  "email": "newemail@example.com"
}
```

### Get Customer with Balance

```bash
GET https://api.kangaroorewards.com/customers/{customer_id}?include=balance
```

## Transactions

### List Transactions

```bash
GET https://api.kangaroorewards.com/transactions
```

### Get Transaction by ID

```bash
GET https://api.kangaroorewards.com/transactions/{transaction_id}
```

### Create Transaction

```bash
POST https://api.kangaroorewards.com/transactions
Body:
{
  "customer_id": "CUSTOMER_ID",
  "amount": 50.00,
  "name": "Purchase"
}
```

## Offers

### List Offers

```bash
GET https://api.kangaroorewards.com/offers
```

### Create Basic Offer (Coupon)

```bash
POST https://api.kangaroorewards.com/offers
Body:
{
  "type_id": 9,
  "targeted_offer_flag": 1,
  "discount_value": 10,
  "never_expires_flag": 0,
  "expires_at": "2024-12-31T23:59:59+00:00",
  "images": [...],
  "available_at_branches": [...],
  "offer_languages": [...]
}
```

## Rewards

### List Rewards

```bash
GET https://api.kangaroorewards.com/rewards
```

### Redeem Reward

```bash
POST https://api.kangaroorewards.com/customers/{customer_id}/rewards/{reward_id}/redeem
```

## Common Query Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `page` | integer | Page number for pagination | `?page=2` |
| `include` | string | Include related resources | `?include=balance` |
| `relationships` | string | Include relationships | `?relationships=address` |
| `created_at` | string | Filter by creation date | `?created_at=gt\|2023-01-01` |

## Filter Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `gt` | Greater than | `created_at=gt\|2023-01-01` |
| `gte` | Greater than or equal | `amount=gte\|100` |
| `lt` | Less than | `points=lt\|500` |
| `lte` | Less than or equal | `amount=lte\|1000` |
| `eq` | Equal to | `email=eq\|user@example.com` |

## HTTP Status Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Request completed successfully |
| 201 | Created | Resource created successfully |
| 204 | No Content | Resource deleted successfully |
| 400 | Bad Request | Check request format and parameters |
| 401 | Unauthorized | Refresh access token |
| 403 | Forbidden | Check permissions and scopes |
| 404 | Not Found | Verify resource ID |
| 422 | Validation Error | Check request body for errors |
| 429 | Rate Limited | Implement backoff and retry |
| 500 | Server Error | Contact support if persistent |

## Rate Limits

- **Limit:** 240 requests per minute per OAuth token or IP
- **Headers:**
  - `X-RateLimit-Limit`: Maximum requests per minute
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Unix timestamp when limit resets

## Required Headers

Every request must include:

```
Authorization: Bearer ACCESS_TOKEN
X-Application-Key: YOUR_APP_KEY
Accept: application/vnd.kangaroorewards.api.v1+json
```

For POST/PUT/PATCH requests, also include:

```
Content-Type: application/json
```

## Common Includes

### Customers
- `balance` - Customer's points and giftcard balance
- `tier_level` - Customer's current tier level
- `tier_progress` - Customer's tier progression
- `tiers` - Available tiers
- `referral_programs` - Referral program details

### Transactions
- `customer` - Customer object
- `purchase.receipt` - Receipt details
- `transaction_sequences` - Related transactions
- `transaction_details` - Transaction details

## Date Format

All dates must be in ISO 8601 format:

```
2024-01-15T14:30:00+00:00
```

## Common Error Responses

### 401 Unauthorized
```json
{
  "error": {
    "status_code": 401,
    "message": "Unauthenticated",
    "description": "The access token is invalid or has expired"
  }
}
```

### 422 Validation Error
```json
{
  "email": ["The email field is required"],
  "phone": ["The phone field must be a valid phone number"]
}
```

## Best Practices Checklist

- ✓ Use HTTPS for all requests
- ✓ Store access tokens and secrets securely
- ✓ Implement token refresh logic
- ✓ Handle rate limiting with exponential backoff
- ✓ Validate request data before sending
- ✓ Log API errors for debugging
- ✓ Use pagination for large datasets
- ✓ Cache frequently accessed data
- ✓ Include proper error handling
- ✓ Monitor API usage and performance

## SDKs

- **PHP:** [KangarooRewards-PHP-SDK](https://github.com/kangaroorewards/KangarooRewards-PHP-SDK)
- **OAuth2:** [OAuth2 Kangaroo Rewards](https://github.com/kangaroorewards/oauth2-kangaroo-rewards)

## Support

- **Documentation:** https://api.kangaroorewards.com/docs
- **Developer Portal:** https://api.kangaroorewards.com/developers
- **Tutorials:** https://github.com/kangaroorewards/api-docs/wiki
