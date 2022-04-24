import React, { useState } from 'react';
import MapView, { Marker, Callout, Circle, CalloutSubview } from 'react-native-maps';
import Slider from '@react-native-community/slider';
import { StyleSheet, Text, View, Dimensions } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import axios from 'axios';

const MapScreen = (props) => {
  // const [pin, setPin] = useState({
  //   latitude: 40.758896, 
  //   longitude: -73.985130,
  // });
  console.log(props.pin)
  const [rad, setRad] = useState(500);
  return (
    <View style={styles.container}>
      <MapView style={styles.map} 
        initialRegion = {{
          latitude: 40.758896, 
          longitude: -73.985130,
          latitudeDelta: 0.05,
          longitudeDelta: 0.03
        }}
        provider = "google"
      > 
        <Marker
          coordinate={{
            latitude: 40.758896, 
            longitude: -73.985130,
          }}
          draggable={true}
          onDragStart={(e) => {
            console.log("Start drag", e.nativeEvent.coordinate)
          }}
          onDragEnd={(e) => {
            props.setPin({
              latitude: e.nativeEvent.coordinate.latitude,
              longitude: e.nativeEvent.coordinate.longitude
            })
            console.log("Stop drag", e.nativeEvent.coordinate)
          }}
        >
          <Callout
            // Use this onPress to save state and go to rest of quiz
            onPress={() => {
              console.log(props.pin);
              axios.post('http://127.0.0.1:8000/quiz-map', props.pin
              ).then((response) => console.log(response)
              ).catch((error) => console.log(error))
              props.navigation.navigate("SocialScreen")
            }}
          >
            <Text> CLICK TO SAVE </Text>
          </Callout>
        </Marker>
        <Circle
          center={props.pin}
          radius={rad}
        />
      </MapView>
      <View style={styles.slidercontainer}>
          <Slider
            style={styles.slider}
            minimumValue={500}
            maximumValue={2000}
            value={1250}
            onValueChange={(value) => setRad(value)}
          />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  map: {
    width: Dimensions.get('window').width,
    height: Dimensions.get('window').height,
  },
  slider: {
    position: 'absolute',
    flex: 1,
    marginLeft: 10,
    marginRight: 10,
    alignItems: 'stretch',
    justifyContent: 'center',
},
  slidercontainer: {
    position:'absolute', 
    bottom: 75, 
    width: 425, 
    height: 60 , 
    alignSelf: 'center',
    backgroundColor: '#F5FFFA',
  },
  slider: {
    justifyContent: "center",
    width:400, 
    height:40
  }
});

export default MapScreen;