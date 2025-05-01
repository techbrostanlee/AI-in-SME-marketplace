# AI-in-SME-marketplace
Master's project by Stanislaus Igbo
# AI-Powered Personalized Product Recommendations for SME E-Commerce

A functional prototype e-commerce platform for Small and Medium-sized Enterprises (SMEs), featuring an AI-driven content-based product recommendation engine. Developed using Flask, SQLite, and modern web technologies, this project demonstrates how SMEs can leverage artificial intelligence to deliver personalized shopping experiences, enhance customer engagement, and improve sales performance-while overcoming common barriers such as limited resources and technical expertise.

---

## **Project Overview**

This project implements a scalable, cost-effective AI-powered recommendation system tailored for SME marketplaces. It uses content-based filtering (CBF) techniques-specifically TF-IDF vectorization and cosine similarity-to generate personalized product suggestions based on user behaviour and product attributes. The platform includes essential e-commerce features such as user registration, product categorization, shopping cart functionality, and secure authentication.

---

## **Key Features**

- User registration, authentication, and profile management (including profile picture upload)
- Product listing and categorization
- Shopping cart and checkout functionality
- AI-driven content-based product recommendation engine
- Simple consent mechanism for AI recommendations
- Secure session management
- Built using Flask (Python), SQLite (via SQLAlchemy), HTML, CSS, and JavaScript

---

## **Motivation**

SMEs face significant challenges in adopting AI, including limited resources, technical expertise, and integration difficulties. This project bridges the digital divide by providing a practical, user-centered AI solution that empowers SMEs to compete with larger e-commerce players and deliver personalized customer experiences.

---

## **Project Scope**

- **Included:**
  - Functional e-commerce prototype for SMEs
  - Content-based recommendation engine (TF-IDF, cosine similarity)
  - User and product management
  - Basic consent and privacy features

- **Excluded:**
  - Third-party payment gateway integration (e.g., PayPal, Stripe)
  - Shipping/logistics tracking
  - Real-time inventory management
  - Multi-vendor support and advanced analytics
  - Collaborative filtering or deep learning models

---

## **Architecture & Technologies**

- **Backend:** Flask (Python)
- **Database:** SQLite (SQLAlchemy ORM)
- **Frontend:** HTML, CSS, JavaScript
- **AI Recommendation Engine:** Content-based filtering (TF-IDF, cosine similarity)
- **Dataset:** Curated Amazon Sales Dataset (from Kaggle)

---

## **Installation & Setup**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/techbrostanlee/AI-in-SME-marketplace.git
   cd AI-in-SME-marketplace
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Initialize the database:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. **Run the application:**
   ```bash
   flask run
   ```

---

## **Usage**

- Register as a new user and log in.
- Browse and search products.
- Add products to your cart and proceed to checkout.
- Receive AI-powered product recommendations based on your browsing and purchase history.

---

## **Project Management Approach**

- **Methodologies:** Object-Oriented Analysis and Design Methodology (OOADM), Agile frameworks
- **Practices:** Iterative development, version control (Git), risk management, and regular milestones

---

## **Assumptions & Constraints**

- Users have internet access and basic e-commerce familiarity.
- Product data includes meaningful attributes (name, category, description, tags).
- The system is designed for prototype/demo purposes and is not production-ready.
- Local static directories are used for image storage (not cloud-based).
- Limited to small-scale testing (SQLite, no high concurrency).

---

## **Future Work**

- Integration of collaborative filtering and hybrid recommendation models
- Payment gateway and logistics integration
- Cloud-based storage and scalability enhancements
- Advanced analytics and admin dashboards

---

## **Acknowledgements**

- Developed as part of MSc IT Project Management at Teesside University
- Supervisor: Nawaz, Mansha
- Second Reader: Hopkinson, Glen

---

## **License**

This project is for academic and demonstration purposes. Please refer to the LICENSE file for details.

---

## **Contact**

For questions or collaboration:
- **Author:** Igbo Stanislaus Chimere
- **Email:** [stanleyike54@gmail.com]

---

> *“This project demonstrates the feasibility of implementing cost-effective AI solutions in SME marketplaces, bridging the digital divide and empowering smaller businesses to compete effectively in the global digital economy.”*


