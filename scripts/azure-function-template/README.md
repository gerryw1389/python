# ReadJSON

This is a HTTP triggered python app running in Azure Functions that:

1. You pass a two level json payload and it will put them in variables

   ```json
   {
      "name": "gerry-ReadJSON3",
      "car": "mustang-ReadJSON3",
      "birth": {
         "city": "fort worth-ReadJSON3",
         "state": "Texas-ReadJSON3"
      }
   }
   ```

   - Response:

   ```
   Hello, gerry-ReadJSON3.

   You chose mustang-ReadJSON3.

   Your birth city is fort worth-ReadJSON3 in the state of Texas-ReadJSON3
   ```

2. You can call any of the three functions `ReadJSON`, `ReadJSON2`, or `ReadJSON3`
  - Inside function apps, find the `App Key` blade in Azure and copy the `_master` key
  - Paste it on the end of each URL: `https://{yourApp}.azurewebsites.net/api/ReadJSON?code={_masterKey}`

3. Each of them can import a `helpers.py` function so you can put functions in their own files :)

4. For logging, I tried to modify the `host.json` so that most things are dropped except output.

5. Added a `shared` folder that all functions within the app can use. See `ReadJSON` for calling first function in `shared/shared.py` and `ReadJSON2` for calling second function in `shared/shared.py`

6. Added a way for it to return a json response instead of text (see `ReadJSON`).

  ```json
  [{"response": "Hello, gerry-ReadXML.\n\nYou chose mustang-ReadXML.\n\nYour birth city is fort worth-ReadXML in the state of Texas-ReadXML", "date_time": "2020-11-30-21-23-29"}]
  ```