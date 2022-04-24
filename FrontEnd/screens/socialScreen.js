import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import { View, StyleSheet, TouchableOpacity, Text} from 'react-native';
import { TextInput } from 'react-native-gesture-handler';
import axios from "axios";
import { useState } from 'react';
import { MapScreen } from './mapScreen'


const SocialScreen = () => {
    const [foodList, setFoodList] = useState([]);
    return(
        <View style = {styles.container}>
          <Text style={{ fontSize: 25 }}> Form Quiz Section </Text>
        <Formik
          initialValues={{food: '',distance: '',latitude: '', longitude: '',price: '' }}
          onSubmit={(values) => {
            console.log(values);
            axios.post('http://127.0.0.1:8000/quiz-form', values
            ).then(function (response) {
              console.log(response.data);
              setFoodList(response.data);
            }).catch(function (error) {
              console.log(error);
            })
          }}
        >
        {({ handleChange, handleBlur, handleSubmit, values }) => (
          <View>
            <TextInput
              style = {styles.formInput}
              placeholder = "Food (Chinese, American, etc.)"
              onChangeText={handleChange('food')}
              onBlur={handleBlur('food')}
              value={values.food}
            />
            <TextInput
              placeholder = "Price (1-4)"
              style = {styles.formInput}
              onChangeText={handleChange('price')}
              onBlur={handleBlur('price')}
              value={values.price}
            />
            <TouchableOpacity
              style={styles.button}
              onPress={handleSubmit} >
              <Text style={styles.buttonText}> Submit </Text>
            </TouchableOpacity>
            {
              foodList.length >= 1 ? foodList.map((food, idx) => {
                return <View style = {styles.food}>
                        <Text style = {styles.buttonText} key = {idx}>{food.name} : {food.address}</Text>
                      </View>
              }): <Text></Text>
            }
          </View>
        )}
      </Formik>
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
    formInput: {
      borderWidth: 1,
      borderColor: '#ddd',
      padding: 10,
      fontSize: 18,
      borderRadius: 6,
    },
    button: {
      alignItems: 'center',
      justifyContent: 'center',
      paddingVertical: 12,
      paddingHorizontal: 32,
      borderRadius: 4,
      elevation: 3,
      backgroundColor: 'black',
    },
    buttonText: {
      fontSize: 18,
      color: '#ffffff',
      alignSelf: 'center'
    },
    food: {
      alignItems: 'center',
      justifyContent: 'center',
      paddingVertical: 12,
      paddingHorizontal: 32,
      borderRadius: 4,
      elevation: 3,
      backgroundColor: 'darkslateblue',
    },
  })


export default SocialScreen;