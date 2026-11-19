const API_URL = "http://127.0.0.1:8000/predict";

const form = document.querySelector("#prediction-form");
const smokerOptions = document.querySelectorAll('input[name="currentSmoker"]');
const cigarettesInput = document.querySelector("#cigsPerDay");
const cigarettesHint = document.querySelector("#cigs-hint");
const submitButton = document.querySelector("#submit-button");
const resultCard = document.querySelector("#result-card");
const resultHeading = document.querySelector("#result-heading");
const resultMessage = document.querySelector("#result-message");
const resultDetails = document.querySelector("#result-details");
const probabilityValue = document.querySelector("#probability-value");
const probabilityBar = document.querySelector("#probability-bar");
const progressTrack = document.querySelector(".progress-track");

smokerOptions.forEach((option) => {
  option.addEventListener("change", () => {
    const isSmoker = document.querySelector('input[name="currentSmoker"]:checked')?.value === "1";
    cigarettesInput.disabled = !isSmoker;
    cigarettesInput.required = isSmoker;
    cigarettesInput.value = isSmoker ? "" : "0";
    cigarettesHint.textContent = isSmoker ? "Ingresá una cantidad entre 0 y 70." : "Se enviará 0 si no fuma.";
  });
});

function showError(message) {
  resultCard.classList.remove("is-positive", "is-negative");
  resultCard.classList.add("has-error");
  resultHeading.textContent = "No se pudo obtener la predicción";
  resultMessage.textContent = message;
  resultDetails.hidden = true;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  if (!form.reportValidity()) return;

  const formData = new FormData(form);
  const payload = {
    male: Number(formData.get("male")),
    age: Number(formData.get("age")),
    education: Number(formData.get("education")),
    currentSmoker: Number(formData.get("currentSmoker")),
    cigsPerDay: Number(formData.get("cigsPerDay")),
    BPMeds: Number(formData.get("BPMeds")),
    prevalentStroke: Number(formData.get("prevalentStroke")),
    prevalentHyp: Number(formData.get("prevalentHyp")),
    diabetes: Number(formData.get("diabetes")),
    totChol: Number(formData.get("totChol")),
    sysBP: Number(formData.get("sysBP")),
    diaBP: Number(formData.get("diaBP")),
    BMI: Number(formData.get("BMI")),
    heartRate: Number(formData.get("heartRate")),
    glucose: Number(formData.get("glucose")),
  };

  submitButton.disabled = true;
  submitButton.querySelector(".button-label").textContent = "Consultando modelo...";
  resultCard.classList.remove("has-error", "is-positive", "is-negative");
  resultHeading.textContent = "Procesando datos";
  resultMessage.textContent = "Estamos esperando la respuesta de la API.";
  resultDetails.hidden = true;

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const error = await response.json().catch(() => null);
      const detail = Array.isArray(error?.detail)
        ? "Revisá los valores ingresados e intentá nuevamente."
        : error?.detail;
      throw new Error(detail || `La API respondió con el estado ${response.status}.`);
    }

    const data = await response.json();
    const percentage = Number(data.porcentaje);
    if (!Number.isFinite(percentage) || !data.resultado) {
      throw new Error("La respuesta de la API no tiene el formato esperado.");
    }

    const positive = Number(data.prediccion) === 1;
    resultCard.classList.toggle("is-positive", positive);
    resultCard.classList.toggle("is-negative", !positive);
    resultHeading.textContent = data.resultado;
    resultMessage.textContent = positive
      ? "El modelo estimó una probabilidad más elevada para la clase positiva."
      : "El modelo estimó una probabilidad más baja para la clase positiva.";
    probabilityValue.textContent = `${percentage.toFixed(2)}%`;
    probabilityBar.style.width = `${Math.min(100, Math.max(0, percentage))}%`;
    progressTrack.setAttribute("aria-valuenow", String(Math.min(100, Math.max(0, percentage))));
    resultDetails.hidden = false;
  } catch (error) {
    showError(error instanceof TypeError
      ? "No pudimos conectar con la API. Verificá que el backend esté iniciado y volvé a intentar."
      : error.message);
  } finally {
    submitButton.disabled = false;
    submitButton.querySelector(".button-label").textContent = "Obtener predicción";
  }
});