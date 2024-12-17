public class MainActivity : AppCompatActivity
    {
        WebView mWebview;
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            Xamarin.Essentials.Platform.Init(this, savedInstanceState);           

            mWebview = new WebView(this);
            mWebview.Settings.JavaScriptEnabled = true; 
            mWebview.Settings.DomStorageEnabled = true;
            mWebview.Settings.BuiltInZoomControls = true; 
            mWebview.Settings.DisplayZoomControls = false;
            mWebview.Settings.CacheMode = CacheModes.NoCache;

            mWebview.LoadUrl($"file:///android_asset/Content/login.html");
            SetContentView(mWebview); 
        }
        public override void OnRequestPermissionsResult(int requestCode, string[] permissions, [GeneratedEnum] Android.Content.PM.Permission[] grantResults)
        {
            Xamarin.Essentials.Platform.OnRequestPermissionsResult(requestCode, permissions, grantResults);

            base.OnRequestPermissionsResult(requestCode, permissions, grantResults);
        }
    }
    public class JavaScriptInterface : Java.Lang.Object
    {
        [JavascriptInterface]
        [Export("alert")] 
        public void alert(string data)
        {
            Toast.MakeText(Application.Context, data, ToastLength.Short).Show();
        }
    }
