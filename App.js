import { useState } from "react";
import BinarySearchTree from "./bst";
import circle from "./circle.png";

var tree = new BinarySearchTree();

function App() {
  const [input, setInput] = useState("");
  const [array, setArray] = useState([]);
  const [uToPrintArray, setUToPrintArray] = useState([]);
  const [find, setFind] = useState("false");

  function handleSubmit() {
    if (input.length > 5) return;
    var node = tree.insert(input);
    console.log(tree);
    setArray(
      array.concat([
        <div key={array.length - 100}>
          <img
            className="image"
            alt="imageCantBeLoaded"
            src={circle}
            key={array.length}
            style={{
              position: "absolute",
              top: node.y,
              left: node.x,
              width: 40,
              height: 40,
            }}
          />
          <div
            key={array.length - 200}
            style={{
              position: "absolute",
              top: node.y + 10,
              left: node.x + 20 - 4 * input.length,
            }}
          >
            {input}
          </div>
        </div>,
      ])
    );
  }

  function _handleKeyDown(e) {
    if (e.key === "Enter") {
      handleSubmit();
    }
  }

  function handlePrint() {
    var toPrintArray = tree.printTreeInOrder();
    setUToPrintArray(
      toPrintArray.map((number) => <div key={number}>{number}</div>)
    );
  }

  function handleFind() {
    let arr = tree.printTreeInOrder();
    console.log(arr);
    if (arr.includes(input)) {
      console.log("yes");
      setFind("true");
    } else {
      setFind("false");
    }
  }

  return (
    <div>
      <label>
        Input
        <input
          type="number"
          name="inputName"
          value={input}
          onKeyDown={_handleKeyDown}
          onChange={
            (e) => setInput(e.target.value)
            //e.target.value < 6 ? setInput(e.target.value) : console.log("else")
          }
        />
      </label>
      <button type="submit" onClick={handleSubmit}>
        Submit
      </button>
      <button type="submit" onClick={handlePrint}>
        Print
      </button>
      <button type="submit" onClick={handleFind}>
        Find
      </button>
      <div>{array}</div>
      <div>{find}</div>
      <div>{uToPrintArray}</div>
    </div>
  );
}

export default App;
