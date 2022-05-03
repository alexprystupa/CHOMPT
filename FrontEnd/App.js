import React, { useState } from 'react';
import ProfileScreen from './screens/profileScreen'
import MapScreen from './screens/mapScreen';
import SocialScreen from './screens/socialScreen';
import { Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Tabs from './components/Tabs'

const Stack = createNativeStackNavigator();

const App = () => {
  // const [pin, setPin] = useState({
  //   latitude: 40.758896, 
  //   longitude: -73.985130,
  // });
  return(
    <NavigationContainer>
      <Stack.Navigator
        screenOptions={{
          headerShown: false
        }}
      >
        <Stack.Screen
          name = "ProfileScreen"
          component = { Tabs }
        />
        <Stack.Screen
        name = "SocialScreen"
        component = { Tabs }
        options={{title: "Form Quiz Section"
        //, presentation: "modal"
          }}
        />
        <Stack.Screen
        name = "MapScreen"
        component = { Tabs }
        />
      </Stack.Navigator>
    </NavigationContainer>
  )
}

export default App;
