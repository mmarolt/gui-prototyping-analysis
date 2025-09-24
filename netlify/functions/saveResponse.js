import { google } from "googleapis";
import { readFileSync } from "fs";

export async function handler(event) {
    try {
        if (event.httpMethod !== "POST") {
            return { statusCode: 405, body: "Method Not Allowed" };
        }

        const data = JSON.parse(event.body);

        const credentials = JSON.parse(readFileSync("magistrska-472716-ef25e97968f7.json"));

        const auth = new google.auth.JWT(
            credentials.client_email,
            null,
            credentials.private_key,
            ["https://www.googleapis.com/auth/spreadsheets"]
        );

        const sheets = google.sheets({ version: "v4", auth });

        const spreadsheetId = "1dAFQnBIkarG_N2pjD6xHnI66He3Xx3yl_0h4pbFd9w4";
        const range = "List1!A:AH";

        await sheets.spreadsheets.values.append({
            spreadsheetId,
            range,
            valueInputOption: "RAW",
            requestBody: {
                values: [[new Date().toISOString(), ...Object.values(data)]],
            },
        });

        return { statusCode: 200, body: "Success" };
    } catch (error) {
        return { statusCode: 500, body: error.toString() };
    }
}
