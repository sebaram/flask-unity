using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;

public class GetDisplayIMG : MonoBehaviour
{
    public GameObject rawImage;
    public string img_url_pre = "http://localhost:12572/id/";

    IEnumerator  DlImage(object[] parms){   
        Debug.Log("DownloadImage: call");

        RawImage img = (RawImage)parms[0];
        UnityWebRequest request = UnityWebRequestTexture.GetTexture((string)parms[1]);
        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.ConnectionError ||
            request.result == UnityWebRequest.Result.ProtocolError){
                Debug.LogError(request.error);
        }
        else{

            img.texture = ((DownloadHandlerTexture) request.downloadHandler).texture;
            Debug.Log("DownloadImage: texture set");
        }
            
    }


    // Start is called before the first frame update
    void Start()
    {
        rawImage = GameObject.Find ("RawImage");
    
    }


    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Alpha0)) {
            object[] parms = new object[2]{rawImage.GetComponent<RawImage> (), img_url_pre+"0"};
            StartCoroutine("DlImage", parms);

        }
        else if (Input.GetKeyDown(KeyCode.Alpha1)) {
            object[] parms = new object[2]{rawImage.GetComponent<RawImage> (), img_url_pre+"1"};
            StartCoroutine("DlImage", parms);

        }
        else if (Input.GetKeyDown(KeyCode.Alpha2)) {
            object[] parms = new object[2]{rawImage.GetComponent<RawImage> (), img_url_pre+"2"};
            StartCoroutine("DlImage", parms);

        }
        else if (Input.GetKeyDown(KeyCode.Alpha3)) {
            object[] parms = new object[2]{rawImage.GetComponent<RawImage> (), img_url_pre+"3"};
            StartCoroutine("DlImage", parms);

        }
    }
}



