//
//  features.h
//  TouchRecord
//
//  Created by Julia Schwarz on 8/9/13.
//
//

#ifndef TouchRecord_features_h
#define TouchRecord_features_h

#include <math.h>

struct list_feature {
    float mean;
    float std;
    float min;
    float max;
};

struct window_features {
    int num_events;
    int num_other_events;
    struct list_feature dist;
    struct list_feature major_axis;
    struct list_feature speed;
    struct list_feature accel;
};

struct features {
    struct window_features window_features_50;
    struct window_features window_features_100;
    struct window_features window_features_200;
    struct window_features window_features_300;
    struct window_features window_features_400;
    struct window_features window_features_500;
    struct window_features window_features_600;
    struct window_features window_features_700;
    struct window_features window_features_800;
    struct window_features window_features_900;
    struct window_features window_features_1000;
};

#endif
