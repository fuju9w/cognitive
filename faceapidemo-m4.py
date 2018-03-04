########### sample of calling FaceAPI from Python 3.6 #############
## @fujute : March4,2018
##  This is modified version from original code from " https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236 "
##
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'PLEASE REPLACE THIS TEXT WITH YOUR FACE API KEY',
}
# https://www.microsoft.com/cognitive-services/en-us/face-api 
# reference https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,smile,facialHair,glasses,headPose,emotion',
})

mypictures = ["{ 'url': 'https://raw.githubusercontent.com/fuju9w/cognitive/master/man-crazy-funny-dude-45882.jpg' }","{ 'url': 'https://raw.githubusercontent.com/fuju9w/cognitive/master/peam-m1-2017.jpg' }","{ 'url': 'https://raw.githubusercontent.com/fuju9w/cognitive/master/pexels-photo-372042.jpg' }"]


try:
	conn = http.client.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')	
	for body in mypictures:
		print(body)
		conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()
		print(data)
		print ("------------------------------------------")
	conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################    
