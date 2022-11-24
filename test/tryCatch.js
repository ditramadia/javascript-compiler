try {
  if (x == "") throw "Empty";
  if (isNaN(x)) throw "Not a number";
  if (x > 10) throw "Too high";
  if (x < 5) throw "Too low";
} catch (err) {
  message = "Error: " + err + ".";
} finally {
  value = "";
}
