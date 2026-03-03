const API_BASE = "http://localhost:5000";

export async function scorePage(payload) {
  const response = await fetch(`${API_BASE}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    throw new Error(`Prediction failed with status ${response.status}`);
  }

  return response.json();
}
