import React, { useState, useEffect } from 'react';
import MapView, { Marker, Callout, Circle, CalloutSubview } from 'react-native-maps';
import Slider from '@react-native-community/slider';
import { StyleSheet, Text, View, Dimensions } from 'react-native';
import { NavigationContainer, useNavigation } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import axios from 'axios';
import * as Location from 'expo-location';

const MapScreen = ({ navigation, pin, setPin, rad, setRad }) => {
  //console.log(pin)
  navigation = useNavigation();
  return (
    <View style={styles.container}>
      <MapView style={styles.map} 
        region = {{
          latitude: pin.latitude,
          longitude: pin.longitude,
          latitudeDelta: 0.05,
          longitudeDelta: 0.03,
        }}
        provider = "google"
        showsUserLocation = {true}
        onUserLocationChange = {(e) => {
          console.log("Change location", e.nativeEvent.coordinate);
          setPin({
            latitude: e.nativeEvent.coordinate.latitude,
            longitude: e.nativeEvent.coordinate.longitude
          });
        }}
      > 
        <Marker
          coordinate={pin}
          draggable={true}
          onDragStart={(e) => {
            console.log("Start drag", e.nativeEvent.coordinate)
          }}
          onDragEnd={(e) => {
            setPin({
              latitude: e.nativeEvent.coordinate.latitude,
              longitude: e.nativeEvent.coordinate.longitude
            });
            console.log("Stop drag", e.nativeEvent.coordinate)
          }}
        >
        </Marker>
        <Circle
          center={pin}
          radius={rad}
        />
      </MapView>
      <View style={styles.slidercontainer}>
          <Slider
            style={styles.slider}
            minimumValue={500}
            maximumValue={10000}
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