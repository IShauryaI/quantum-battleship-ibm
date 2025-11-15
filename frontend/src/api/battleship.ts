const attack = async (x: number, y: number) => {
  const res = await fetch("http://127.0.0.1:5000/api/attack", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ x, y }),
  });

  return res.json();
};

