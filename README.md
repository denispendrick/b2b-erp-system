# 📦 B2B ERP System

Enterprise Resource Planning system for B2B companies to manage inventory, orders, invoicing, and vendor relationships across multiple currencies.

## 🚀 Features

### Inventory Management
- Product master data management with SKU tracking
- Multi-warehouse stock tracking
- Real-time inventory levels and reservations
- Stock movements, adjustments, and transfers
- Serial number and batch/lot tracking
- Expiry date management
- Reorder point alerts and low stock notifications
- Stock valuation (FIFO, LIFO, Weighted Average)
- Inventory aging and turnover reports
- ABC analysis

### Order Processing
- **Sales Orders**: Quote management, order confirmation, status tracking, partial fulfillment
- **Purchase Orders**: Supplier quotations, PO approval workflow, GRN, quality inspection
- Order fulfillment with pick lists and packing slips
- Shipping label generation and tracking integration
- Backorder management with automatic creation
- Order history and amendments

### Invoicing
- Auto-generate invoices from sales orders
- Manual and recurring invoice creation
- Customizable invoice templates
- Multi-currency invoice support
- Tax calculation (VAT, GST, Sales Tax)
- Discounts and promotions
- Payment processing and reconciliation
- Credit notes and refund management
- Accounts receivable aging reports
- Payment collection tracking

### Multi-Currency Support
- Multiple currency management
- Exchange rate tracking with auto-updates
- Historical exchange rate records
- Currency conversion on transactions
- Multi-currency reporting
- Currency gain/loss calculation
- Bank account management per currency

### Vendor Management
- Vendor profile and contact management
- Payment terms and credit limits
- Vendor categorization and tax information
- On-time delivery and quality metrics
- Vendor rating system
- Performance scorecards
- Price lists and contract management
- Spend analysis and vendor comparison

### Financial Reporting
- Profit & Loss statements
- Balance sheet
- Cash flow statement
- Trial balance
- Revenue analysis by product/category/customer
- Cost of goods sold (COGS) tracking
- Gross margin analysis
- Budget vs actual reporting
- Real-time KPI dashboard
- Trend and comparative analysis

## 🏗️ Technology Stack

### Frontend
- **Framework**: Vue 3 + Nuxt.js 3
- **UI**: Tailwind CSS
- **State Management**: Pinia
- **Charts**: Chart.js + Vue-Chartjs
- **Forms**: VeeValidate + Yup
- **Data Fetching**: TanStack Query (Vue Query)
- **HTTP Client**: Axios

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15
- **ORM**: SQLAlchemy 2.0
- **Migrations**: Alembic
- **Task Queue**: Celery + Redis
- **Authentication**: JWT (python-jose)
- **PDF Generation**: ReportLab
- **Excel Export**: Pandas + OpenPyXL

### Infrastructure
- **Containerization**: Docker + Docker Compose
- **Cache**: Redis
- **API Documentation**: Auto-generated (Swagger/OpenAPI)

## 📋 Prerequisites

- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- PostgreSQL 15+ (if running locally)

## 🚀 Quick Start

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd b2b-erp-system
```

2. Start all services:
```bash
docker-compose up -d
```

3. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Local Development

#### Backend Setup

1. Navigate to backend directory:
```bash
cd fastapi-app
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run migrations:
```bash
alembic upgrade head
```

6. Start the server:
```bash
uvicorn app.main:app --reload
```

#### Frontend Setup

1. Navigate to frontend directory:
```bash
cd nuxt-app
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Start development server:
```bash
npm run dev
```

## 📚 API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🗄️ Database Schema

The system uses a multi-tenant PostgreSQL database with the following main entities:

- **Organizations**: Multi-tenant support
- **Products**: Product master data
- **Inventory**: Stock levels and movements
- **Sales Orders**: Customer orders
- **Purchase Orders**: Vendor orders
- **Invoices**: Billing and payments
- **Vendors**: Supplier management
- **Currencies**: Multi-currency support
- **Exchange Rates**: Currency conversions

## 🔐 Security Features

- JWT token-based authentication
- Role-based access control (RBAC)
- Permission-based authorization
- Organization-level data isolation
- Password hashing with bcrypt
- SQL injection prevention
- XSS and CSRF protection
- Rate limiting
- Comprehensive audit trail

## 📊 Key Reports

### Inventory Reports
- Stock Valuation
- Stock Movement
- Inventory Aging
- Reorder Recommendations
- ABC Analysis

### Sales Reports
- Sales by Product/Customer/Period
- Sales Forecast
- Order Fulfillment Rate

### Financial Reports
- Profit & Loss Statement
- Balance Sheet
- Cash Flow Statement
- Accounts Receivable/Payable Aging

### Vendor Reports
- Vendor Spend Analysis
- Vendor Performance Metrics
- Payment History

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **denispendrick** - Initial work

## 🙏 Acknowledgments

- Built with Vue 3 and Nuxt.js
- Powered by FastAPI
- Database: PostgreSQL# Security update 0
# Security update 1
