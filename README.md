# 👨‍💻 Adhil's Portfolio

A high-performance personal portfolio website built entirely in Python using **FastHTML** and styled with **MonsterUI**. This project showcases my experience as a Software Engineer in Data & Python, featuring a fully responsive design, a dynamic theme customization engine, and a glassmorphism UI.

🔗 **Live Demo:** [adhil-portfolio.onrender.com](https://adhil-portfolio.onrender.com)
## ✨ Key Features

* **⚡ Pure Python Stack:** Built with FastHTML (no JavaScript frameworks required).
* **🎨 Dynamic Theme Picker:** Users can customize the site's color scheme (Blue, Zinc, Rose, etc.), radius, and dark/light mode in real-time.
* **📱 Fully Responsive:**
    * **Desktop:** Clean horizontal glass-morphism navigation.
    * **Mobile:** Native-feel "Off-Canvas" sidebar menu with optimized spacing.
* **💨 High Performance:** Powered by `uvicorn` and `Starlette` for blazing fast load times.
* **📧 Interactive Contact:** Functional contact form integrating directly with native mail clients.

## 🛠️ Tech Stack

* **Framework:** [FastHTML](https://fastht.ml/)
* **UI Components:** [MonsterUI](https://monsterui.answer.ai/) (FrankenUI + TailwindCSS)
* **Server:** Uvicorn
* **Deployment:** Render (Docker/Python Environment)

## 🚀 How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Adhil03/portfolio.git](https://github.com/Adhil03/portfolio.git)
    cd portfolio
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the server**
    ```bash
    # Run with hot-reloading for development
    python portfolio.py

    # OR run with Uvicorn (Production style)
    uvicorn portfolio:app --reload
    ```

4.  **Visit the App**
    Open `http://127.0.0.1:5000` (or the port shown in your terminal).

## 📂 Project Structure

* `portfolio.py`: Main application logic and routing.
* `static/`: Contains CSS, images, and the downloadable resume.
* `requirements.txt`: Production dependencies for Render deployment.

---
© 2026 Adhil. Built with ❤️, Python, and a touch of AI.
