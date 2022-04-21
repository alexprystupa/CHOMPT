import React from 'react';
import t from 'tcomb-form-native';
import { View, StyleSheet, TouchableOpacity } from 'react-native';
import Header from '../components/Header';
import LoginButton from '../components/LoginButton';

const User = t.struct({
    email: t.String,
    username: t.String,
    password: t.String,
    food: t.enums({C: 'Chinese', R: 'Russian', M: 'Mexican', E: 'Fast Casual'}, 
    'food'),
    terms: t.Boolean,
  });
  
const Form = t.form.Form;

const ProfileScreen = ({ navigation }) => {
    return(
        <View style = {styles.container}>
            <TouchableOpacity>
                <Header 
                  HeaderName = "CHOMPT PROFILE"
                />
            </TouchableOpacity>
            <Form type={User} />
            <TouchableOpacity>
                <LoginButton />
            </TouchableOpacity>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      paddingTop: 60,
    },
    containerTwo: {
      justifyContent: 'center',
      marginTop: 50,
      padding: 20,
      backgroundColor: '#ffffff',
    },
  })


export default ProfileScreen;