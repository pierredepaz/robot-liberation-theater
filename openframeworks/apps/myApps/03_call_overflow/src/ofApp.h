#pragma once

#include "ofMain.h"
#include "ofxOsc.h"
#include "Bubble.h"
#include "ofxSyphon.h"

#define PORT 2046

class ofApp : public ofBaseApp{
    
    ofFbo fbo;
    ofxSyphonServer syphon_server;

	public:
		void setup();
		void update();
		void draw();

		void keyPressed(int key);
		void keyReleased(int key);
		void mouseMoved(int x, int y );
		void mouseDragged(int x, int y, int button);
		void mousePressed(int x, int y, int button);
		void mouseReleased(int x, int y, int button);
		void mouseEntered(int x, int y);
		void mouseExited(int x, int y);
		void windowResized(int w, int h);
		void dragEvent(ofDragInfo dragInfo);
		void gotMessage(ofMessage msg);

		bool gotOscMessage();
		
		ofxOscReceiver receiver;
		ofTrueTypeFont font;
		bool started = false;

		string siteUrl = "http://nyuad.im/call-overflow";

		vector<vector<Bubble>> messages;

		int ovrState = 0;
		vector<vector<vector<string>>> ovrMss;
};
