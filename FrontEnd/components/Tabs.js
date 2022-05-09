import React, { useState, useEffect } from 'react'
import {View, Text, StyleSheet, Image, Button} from 'react-native'
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs'
import HomeScreen from '../screens/loginScreen'
import QuizScreen from '../screens/mapScreen'
import SocialScreen from '../screens/socialScreen'
import { useNavigation } from '@react-navigation/native'
import * as Location from 'expo-location';

const Tab = createBottomTabNavigator();

const Tabs = ({ navigation }) => {
    const [pin, setPin] = useState({
        latitude: 40.758896, 
        longitude: -73.985130,
    });
    const [rad, setRad] = useState(500);

    //const [location, setLocation] = useState(null);
    //const [errorMsg, setErrorMsg] = useState(null);
  
    // useEffect(() => {
    //   (async () => {
    //     let { status } = await Location.requestForegroundPermissionsAsync();
    //     if (status !== 'granted') {
    //       setErrorMsg('Permission to access location was denied');
    //       return;
    //     }
  
    //     let pin = await Location.getCurrentPositionAsync({});
    //     setPin({
    //         latitude: pin.coords.latitude,
    //         longitude: pin.coords.longitude,
    //     });
    //   })();
    // }, []);
  
    // let text = 'Waiting..';
    // if (errorMsg) {
    //   text = errorMsg;
    // } else if (pin) {
    //   //console.log(pin.coords.latitude);
    //   //console.log(pin.coords.longitude);
    //   console.log(pin)
    // }

    return (
        <Tab.Navigator
            screenOptions = {{
                tabBarShowLabel: false,
                tabBarStyle: {
                    position: 'absolute',
                    bottom: 0,
                    left: 0,
                    right: 0,
                    elevation: 0,
                    backgroundColor: '#ffffff',
                    borderRadius: 0,
                    height: 90,
                }
            }}
        >
            <Tab.Screen name = "Map Quiz Section" options = {{
                tabBarIcon: ({focused}) => (
                    <Image 
                        source = {require('../assets/icons/bread.png')}
                        resizeMode = 'contain'
                        style = {{
                            width: 60,
                            height: 60,
                            tintColor: focused ? '#e32f45': '#748c94'
                        }}
                    />
                ),
                headerRight: () => {
                    return(
                    <Button
                      onPress={() => navigation.navigate('SocialScreen', { screen: 'Social' })}
                      title="Next"
                      color="black"
                    />
                    )
                },
            }}
            children={() => <QuizScreen pin={pin} setPin={setPin} rad={rad} setRad={setRad}/>}
            />
            <Tab.Screen name = "Social" options = {{
                tabBarIcon: ({focused}) => (
                    <Image 
                        source = {require('../assets/icons/hotdog.png')}
                        resizeMode = 'contain'
                        style = {{
                            width: 60,
                            height: 60,
                            tintColor: focused ? '#e32f45': '#748c94'
                        }}
                    />
                ),
                headerLeft: () => {
                    return(
                    <Button
                      onPress={() => navigation.navigate('MapScreen', { screen: "Map Quiz Section" })}
                      title="Back"
                      color="black"
                    />
                    )
                },
            }}
            children={() => <SocialScreen pin={pin} rad={rad}/>}
            />
        </Tab.Navigator>
    );
}

export default Tabs;