import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONException;
import org.json.JSONObject;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

public class MainActivity extends AppCompatActivity {

    private EditText nameEditText;
    private EditText birthdateEditText;
    private TextView responseTextView;
    private Button fetchHoroscopeButton;
    private RequestQueue requestQueue;

    private static final String SERVER_URL = "http://your_server_ip:8080/horoscope";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        nameEditText = findViewById(R.id.nameEditText);
        birthdateEditText = findViewById(R.id.birthdateEditText);
        responseTextView = findViewById(R.id.responseTextView);
        fetchHoroscopeButton = findViewById(R.id.fetchHoroscopeButton);

        requestQueue = Volley.newRequestQueue(this);

        fetchHoroscopeButton.setOnClickListener(v -> fetchHoroscope());
    }

    private void fetchHoroscope() {
        String name = nameEditText.getText().toString();
        String birthdate = birthdateEditText.getText().toString();

        if (name.isEmpty() || birthdate.isEmpty()) {
            responseTextView.setText("Пожалуйста, введите имя и дату рождения");
            return;
        }

        String url = SERVER_URL + "?name=" + URLEncoder.encode(name, StandardCharsets.UTF_8) +
                     "&birthdate=" + URLEncoder.encode(birthdate, StandardCharsets.UTF_8);

        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                response -> {
                    try {
                        JSONObject jsonResponse = new JSONObject(response);
                        String horoscope = jsonResponse.getString("horoscope");
                        responseTextView.setText(horoscope);
                    } catch (JSONException e) {
                        responseTextView.setText("Ошибка при обработке ответа");
                    }
                },
                error -> responseTextView.setText("Ошибка при получении гороскопа: " + error.getMessage())
        );

        requestQueue.add(stringRequest);
    }
}

