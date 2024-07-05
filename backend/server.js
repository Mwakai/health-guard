const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const bcrypt = require("bcrypt");
const sequelize = require("./config/database");
const User = require("./models/User");

const app = express();
app.use(cors());
app.use(bodyParser.json());

const PORT = process.env.PORT || 5000;

sequelize.sync();

/**
 * REGISTER USERS
 */
app.post("/api/register", async (req, res) => {
  const { name, email, password } = req.body;

  try {
    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = await User.create({
      name,
      email,
      password: hashedPassword,
    });

    res.status(200).json({ message: "User registered successfully!" });
  } catch (error) {
    console.error("Error registering user:", error);
    res.status(500).json({ error: "Error registering user" });
  }
});

/**
 * LOGIN USERS
 */
app.post("/api/login", async (req, res) => {
  const { email, password } = req.body;

  try {
    const user = await User.findOne({ where: { email } });

    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    const isPasswordValid = await bcrypt.compare(password, user.password);

    if (!isPasswordValid) {
      return res.status(401).json({ error: "Invalid password" });
    }

    res.status(200).json({ message: "Login successful", user });
  } catch (error) {
    console.error("Error logging in user:", error);
    res.status(500).json({ error: "Error logging in user" });
  }
});

/**
 * QUESTIONNAIRE
 */
app.post("/api/questionnaire", async (req, res) => {
  const { email, age, height, weight, allergies } = req.body;

  try {
    const user = await User.findOne({
      where: { email },
    });

    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    user.age = age;
    user.height = height;
    user.weight = weight;
    user.allergies = allergies;
    await user.save();

    res
      .status(200)
      .json({ message: "Questionnaire submitted successfully", user });
  } catch (error) {
    console.log("Error submitting quest", error);
    res.status(500).json({ error: "Error submitting" });
  }
});

/**
 * FETCH DATA
 */
app.get("/api/user", async (req, res) => {
  const { email } = req.query;
});

app.get("", async (req, res) => {
  const { age, height, weight, allergies } = req.query;

  const recommendations = [
    {
      id: 1,
      name: "Vitamin D",
      description: "Good for bone health and immune support.",
    },
    {
      id: 2,
      name: "Omega-3",
      description: "Supports heart health and reduces inflammation.",
    },
  ];

  res.status(200).json({ recommendations });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
