const { Sequelize, DataTypes } = require("sequelize");

const sequelize = require("../config/database");

const User = sequelize.define("User", {
  name: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  email: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  password: {
    type: DataTypes.STRING,
    allowNull: false,
  },

  age: {
    type: DataTypes.INTEGER,
    allowNull: true,
  },
  height: {
    type: DataTypes.FLOAT,
    allowNull: true,
  },
  weight: {
    type: DataTypes.FLOAT,
    allowNull: true,
  },
  allergies: {
    type: DataTypes.STRING,
    allowNull: true,
  },
});

module.exports = User;
