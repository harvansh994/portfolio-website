document.getElementById("careerForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const skills = document.getElementById("skills").value;
  const interests = document.getElementById("interests").value;
  const education = document.getElementById("education").value;

  document.getElementById("result").innerText = "⏳ Predicting your future career...";

  try{
    const res = await fetch("https://REPLACE_WITH_YOUR_RENDER_URL/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, skills, interests, education }),
    });

    const data = await res.json();
    document.getElementById("result").innerText = data.result || JSON.stringify(data, null, 2);
  }catch(err){
    document.getElementById("result").innerText = "Error connecting to backend. Make sure backend is deployed and the URL is configured in script.js";
    console.error(err);
  }
});
