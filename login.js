document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const role = document.getElementById("role").value;

  if (!role) {
    alert("Please select a role!");
    return;
  }

  if (role === "admin") {
    window.location.href = "admin-dashboard.html";
  } else if (role === "volunteer") {
    window.location.href = "volunteer-dashboard.html";
  } else if (role === "ngo") {
    window.location.href = "ngo-dashboard.html";
  }
});