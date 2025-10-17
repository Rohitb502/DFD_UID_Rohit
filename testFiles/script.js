// Simple UI logic

function showPage(page) {
  console.log("Navigating to:", page);
}

// When user clicks login button
document.getElementById("loginBtn").addEventListener("click", () => {
  showPage("loginPage");
});

// When user submits login form
document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const response = await fetch("/api/login");
  if (response.ok) showPage("dashboardPage");
});

// Logout button
document.getElementById("logoutBtn").addEventListener("click", () => {
  showPage("homePage");
});
