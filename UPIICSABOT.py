from typing import Final
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final= '5919939431:AAGA-m4RGP0FrX76DCIM9af8j5KAGxsuEeY'
BOT_USERNAME: Final='@Upiicsa_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hola, para comenzar escribe o elige alguno de los siguientes comandos relacionados a los temas de las dudas y preguntas más frecuentes de los alumnos hacia el departamento de Gestión Escolar de la UPIICSA.\n\nReinscripción: /reinscripcion\nTrámites: /tramites\nDictámenes: /dictamenes\nETS: /ets\nInscripción: /inscripcion\nBaja de unidades: /bajadeunidades\nBajas: /bajas\nExamenes de saberes previamente adquiridos: /espa\nTrámites con Carga Menor a la Mínima: /cargaMenor\nElectivas: /electivas\nEquivalencias: /equivalencias\n\nOtros:\nPágina de Gestión Escolar de la UPIICSA: /paginaGE\n\nRecuerda que para escribir un comando este debe de comenzar por una "/" seguido de la palabra clave del tema a consultar sin espacios entre palabras')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Puedo ayudarte ')

async def reinscripcion_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reinscripcion_comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Reinscripción.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cuántas materias puedo reinscribir?\nPregunta 2:¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?\nPregunta 3:¿Si cuento con dictamen vigente puedo reinscribirme?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿Cuántas materias puedo reinscribir?'], ['¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?'],['¿Si cuento con dictamen vigente puedo reinscribirme?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(reinscripcion_comandos,reply_markup=reply_markup)

async def tramites_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tramites_comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Trámites.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Dónde puedo solicitar un trámite?\nPregunta 2:¿Cuánto es el tiempo de espera de mi trámite?\nPregunta 3:¿Qué pasa si no puedo ingresar a la plataforma aún con mis datos de acceso?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿Dónde puedo solicitar un trámite?'], ['¿Cuánto es el tiempo de espera de mi trámite?'],['¿Qué pasa si no puedo ingresar a la plataforma aún con mis datos de acceso?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(tramites_comandos,reply_markup=reply_markup)

async def dictamenes_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dictamenes_comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Dictámenes.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Qué dictamen debo de solicitar si estoy desfasado?\nPregunta 2:¿En qué casos debo de solicitar dictamen ZACATENCO?\nPregunta 3:¿Dónde puedo ver la resolución de mi dictamen?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿Qué dictamen debo de solicitar si estoy desfasado?'],[ '¿En qué casos debo de solicitar dictamen ZACATENCO?'],['¿Dónde puedo ver la resolución de mi dictamen?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(dictamenes_comandos,reply_markup=reply_markup)

async def ets_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ets_comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de ETS.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cómo se si tengo derecho a ETS?\nPregunta 2:¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?\nPregunta 3:¿Cómo solicito revisión a un examen ETS?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿Cómo se si tengo derecho a ETS?'], ['¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?'],['¿Cómo solicito revisión a un examen ETS?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(ets_comandos,reply_markup=reply_markup)

async def inscripcion_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    inscripcion_comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Inscripción.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Qué documentos debo de entregar?\nPregunta 2:¿Cómo podré ver mi horario?\nPregunta 3:¿Cómo solicito cambio de turno?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿Qué documentos debo de entregar?'],[ '¿Cómo podré ver mi horario?'],['¿Cómo solicito cambio de turno?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(inscripcion_comandos,reply_markup=reply_markup)

async def bajaDeUnidades_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bajaDeUnidades_comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Baja de unidades.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Si tengo carga menor a la mínima, puedo dar de baja UA?\nPregunta 2:¿Cuánto tiempo tengo para dar de baja UA?\nPregunta 3:¿Puedo dar de baja recurses?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿Si tengo carga menor a la mínima, puedo dar de baja UA?'], ['¿Cuánto tiempo tengo para dar de baja UA?'],['¿Puedo dar de baja recurses?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(bajaDeUnidades_comandos,reply_markup=reply_markup)

async def baja_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    baja_comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Bajas.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Hasta cuándo tengo para darme de baja temporal?\nPregunta 2:¿Hasta cuándo tengo para darme de baja definitiva?\nPregunta 3:¿Una vez que regrese de baja temporal como podré reinscribirme?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿Hasta cuándo tengo para darme de baja temporal?'], ['¿Hasta cuándo tengo para darme de baja definitiva?'],['¿Una vez que regrese de baja temporal como podré reinscribirme?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(baja_comandos,reply_markup=reply_markup)

async def espa_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    espa_comandos ='Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Examenes de Saberes Previamente Adquiridos.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿En que casos debo presentar saberes previamente adquiridos?\nPregunta 2:¿Cuántas veces puedo presentar un examen de saberes previamente adquiridos?\nPregunta 3:¿Qué proceso debo seguir para presentar un examen de saberes previmente adquiridos?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿En que casos debo presentar saberes previamente adquiridos?'], ['¿Cuántas veces puedo presentar un examen de saberes previamente adquiridos?'],['¿Qué proceso debo seguir para presentar un examen de saberes previmente adquiridos?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(espa_comandos,reply_markup=reply_markup)

async def cargaMenor_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cargaMenor_comandos ='Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Trámites con Carga Menor a la Mínima.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cuándo me corresponde la carta por carga menor a la mínima?\nPregunta 2:¿Cuándo me corresponde dictamen  por carga menor a la mínima?\nPregunta 3:¿Si tengo un dictamen vigente que me permitió reinscribirme, debo de solicitar la carta o el dictamen?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿Cuándo me corresponde la carta por carga menor a la mínima?'], ['¿Cuándo me corresponde dictamen  por carga menor a la mínima?'],['¿Si tengo un dictamen vigente que me permitió reinscribirme, debo de solicitar la carta o el dictamen?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(cargaMenor_comandos,reply_markup=reply_markup)

async def electivas_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    electivas_comandos ='Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Electivas.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cuándo procede un dictamen UPIICSA para acreditar Electivas?\nPregunta 2:¿Cuándo procede un dictamen Zacatenco para acreditar Electivas?\nPregunta 3:¿En cuánto tiempo se verá reflejada mi electiva en kardex?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿Cuándo procede un dictamen UPIICSA para acreditar Electivas?'],[ '¿Cuándo procede un dictamen Zacatenco para acreditar Electivas?'],['¿En cuánto tiempo se verá reflejada mi electiva en kardex?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(electivas_comandos,reply_markup=reply_markup)

async def equivalencias_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    equivalencias_comandos ='Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Equivalencias.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cuáles son las equivalencias que pueden aplicar en mi trayectoria académica?\nPregunta 2:¿Cuánto tiempo tarda en verse reflejadas mis equivalencias?\nPregunta 3:¿Cuántas equivalencias puedo tener?\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    button_labels = [['¿Cuáles son las equivalencias que pueden aplicar en mi trayectoria académica?'],[ '¿Cuánto tiempo tarda en verse reflejadas mis equivalencias?'],['¿Cuántas equivalencias puedo tener?']]
    reply_markup = ReplyKeyboardMarkup(button_labels, resize_keyboard=True)
    await update.message.reply_text(equivalencias_comandos,reply_markup=reply_markup)

async def pagina_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    PAGINA_GESTION_ESCOLAR = 'https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html'
    text='La página de Gestión Escolar de la UPIICSA es:' + PAGINA_GESTION_ESCOLAR
    await update.message.reply_text(text)




def handle_response(text: str) -> str:
    processed: str=text.lower()
    MENSAJE_REGRESO_MENU = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Reinscripción utiliza el comando: /reinscripcion\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    MENSAJE_REGRESO_MENU_TRAMITES= 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Trámites utiliza el comando: /tramites\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    MENSAJE_REGRESO_MENU_DICTAMENES='Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Dictámenes utiliza el comando: /dictamenes\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    MENSAJE_REGRESO_MENU_ETS='Si deseas seguir viendo las dudas y preguntas relacionadas al tema de ETS utiliza el comando: /ets\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    MENSAJE_REGRESO_MENU_INSCRIPCIONES='Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Inscripción utiliza el comando: /inscripcion\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    MENSAJE_REGRESO_MENU_BAJADEUNIDADES='Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Baja de unidades utiliza el comando: /bajadeunidades\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    MENSAJE_REGRESO_MENU_BAJAS='Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Bajas utiliza el comando: /bajas\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    MENSAJE_REGRESO_MENU_ESPA='Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Examenes de Saberes Previamente Adquiridos utiliza el comando: /espa\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    MENSAJE_REGRESO_MENU_MENOR='Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Trámites con Carga Menor a la Mínima utiliza el comando: /cargaMenor\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    MENSAJE_REGRESO_MENU_ELECTIVAS='Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Electivas utiliza el comando: /electivas\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    MENSAJE_REGRESO_MENU_EQUIVALENCIAS='Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Equivalencias utiliza el comando: /equivalencias\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
    if 'hola' in processed:
            return 'Hola'
    #reinscripcion
    elif text == '¿Cuántas materias puedo reinscribir?':
            return '¿Cuántas materias puedo reinscribir?\n\nSi eres alumno regular cualquier carga académica.\n\nSi eres alumno irregular, tiene derecho entre tu carga mínima y media.\n\nConsultar las cargas en https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html\n\n\n' + MENSAJE_REGRESO_MENU
    elif text == '¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?':
            return '¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?\n\nNo, eres alumno regular cuando al cierre del semestre no cuentas con materias adeudadas.\n\n\n' + MENSAJE_REGRESO_MENU
    elif text == '¿Si cuento con dictamen vigente puedo reinscribirme?':
            return '¿Si cuento con dictamen vigente puedo reinscribirme?\n\nSi, siempre y cuando tu dictamen ZACATENCO o UPIICSA te permita reinscripción.\n\nEn caso de duda consulta con tu asesor de carrera https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#ase\n\n\n' + MENSAJE_REGRESO_MENU
    #tramites
    elif text == '¿Dónde puedo solicitar un trámite?':
            return '¿Dónde puedo solicitar un trámite?\n\nDeberás solicitarlo a través de la plataforma www.tramites.upiicsa.ipn.mx\n\nUsuario: Boleta\n\nContraseña: Apellido paterno en minúsculas.\n\n\n' + MENSAJE_REGRESO_MENU_TRAMITES
    elif text == '¿Cuánto es el tiempo de espera de mi trámite?':
            return '¿Cuánto es el tiempo de espera de mi trámite?\n\nConstancias (estudios, periodo vacacional, servicio social y prácticas) de 5 a 10 días hábiles\n\nBoleta Global de 15 a 20 días hábiles\n\nBoleta Global Certificada de 30 a 40 días hábiles.\n\n\n' + MENSAJE_REGRESO_MENU_TRAMITES
    elif text == '¿Qué pasa si no puedo ingresar a la plataforma aún con mis datos de acceso?':
            return '¿Qué pasa si no puedo ingresar a la plataforma aún con mis datos de acceso?\n\nDeberás comunicarte con tu asesor de carrera\n\nhttps://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#ase\n\n\n' + MENSAJE_REGRESO_MENU_TRAMITES
    #dictamenes
    elif text == '¿Qué dictamen debo de solicitar si estoy desfasado?':
            return '¿Qué dictamen debo de solicitar si estoy desfasado?\n\nSi tu periodo de ingreso es del 17/2 en adelante, deberás solicitar dictamen UPIICSA por oportunidad\n\nSi tu periodo es 17/1 hacía atrás, deberás solicitar dictamen CGC ZACATENCO por oportunidad.\n\n\n' + MENSAJE_REGRESO_MENU_DICTAMENES
    elif text == '¿En qué casos debo de solicitar dictamen ZACATENCO?':
            return '¿En qué casos debo de solicitar dictamen ZACATENCO?\n\nSi tu periodo de ingreso fue del 17/1 hacia atrás debes de solicitar ampliación de plazo para tener derecho a reinscripción\n\nSi tu periodo de ingreso fue del 17/1 hacia atrás y tienes materias adeudadas o desfasas , debes solicitar oportunidad.\n\n\n' + MENSAJE_REGRESO_MENU_DICTAMENES
    elif text == '¿Dónde puedo ver la resolución de mi dictamen?':
            return '¿Dónde puedo ver la resolución de mi dictamen?\n\nSi solicitaste dictamen UPIICSA, directamente en tu SAES en el apartado Dictamenes \n\nSi solicitaste dictamen CGC Zacatenco en la página de UPIICSA https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#dicz\n\n\n' + MENSAJE_REGRESO_MENU_DICTAMENES
    #ets
    elif text == '¿Cómo se si tengo derecho a ETS?':
            return '¿Cómo se si tengo derecho a ETS?\n\nSi estuviste inscrito al periodo correspondiente anterior o cuentas con un dictamen vigente que te permita presentarlo.\n\n\n' + MENSAJE_REGRESO_MENU_ETS
    elif text == '¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?':
            return '¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?\n\nEl profesor deberá solicitar la corrección al departamento de gestión escolar.\n\n\n' + MENSAJE_REGRESO_MENU_ETS
    elif text == '¿Cómo solicito revisión a un examen ETS?':
            return '¿Cómo solicito revisión a un examen ETS?\n\nDeberás solicitarlo al Profesor sinodal con apoyo del jefe de la academia correspondiente.\n\n\n' + MENSAJE_REGRESO_MENU_ETS
    #inscripciones
    elif text == '¿Qué documentos debo de entregar?':
            return '¿Qué documentos debo de entregar?\n\nDeberás subir en archivo PDF a la plataforma www.tramites.upiicsa.ipn.mx y entregar en forma física cuando te sea solicitado, los siguientes:\n-Identificación Oficial\n-Copia Acta de Nacimiento\n-2 Fotografías tamaño infantil\n-Copia CURP\n-Hoja de datos generales ( descárgala aquí https://bit.ly/3r0UVeg ) Original y copia\n-Solicitud de inscripción Original y copia\n-Copia de donativo \n-Copia certificado de bachillerato\n\n\n' + MENSAJE_REGRESO_MENU_INSCRIPCIONES
    elif text == '¿Cómo podré ver mi horario?':
            return '¿Cómo podré ver mi horario?\n\nSe publicará la fecha en la página de UPIICSA, y deberás de ingresar a www.saes.upiics.ipn.mx\nUsuario: Número de Boleta, PP o PE\nPassword: Primeras 4 letras de tu apellido paterno en minúsculas.\n\n\n' +  MENSAJE_REGRESO_MENU_INSCRIPCIONES
    elif text == '¿Cómo solicito cambio de turno?':
            return '¿Cómo solicito cambio de turno?\n\nLos cambios de turno y permutas no se realizan, recuerda que, a partir del 2do semestre, tu puedes elegir las materias y turno a cursar.\n\n\n' + MENSAJE_REGRESO_MENU_INSCRIPCIONES
    #baja de unidades
    elif text == '¿Si tengo carga menor a la mínima, puedo dar de baja UA?':
            return '¿Si tengo carga menor a la mínima, puedo dar de baja UA?\n\nNo es posible según el art 54 del RGE que nos cita “El alumno podrá solicitar baja de UA, en las que se encuentra inscrito en el periodos escolar siempre y cuando mantenga la carga mínima establecida en su plan de estudios.”\n\n\n' + MENSAJE_REGRESO_MENU_BAJADEUNIDADES
    elif text == '¿Cuánto tiempo tengo para dar de baja UA?':
            return '¿Cuánto tiempo tengo para dar de baja UA?\n\nDentro de las primeras 3 semanas una vez iniciado el semestre.\n\n\n' + MENSAJE_REGRESO_MENU_BAJADEUNIDADES
    elif text == '¿Puedo dar de baja recurses?':
            return '¿Puedo dar de baja recurses?\n\nNo es posible según el art 54 “Cuando el alumno esté recursando una unidad de aprendizaje no procederá la baja de la misma.”\n\n\n' + MENSAJE_REGRESO_MENU_BAJADEUNIDADES
    #bajas
    elif text == '¿Hasta cuándo tengo para darme de baja temporal?':
            return '¿Hasta cuándo tengo para darme de baja temporal?\n\nDentro del primer mes iniciado el periodo escolar y por causas de fueza mayor probatorias durante todo el periodo. Se debe consultar las fechas de publicación y proceso a seguir en https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#baj\n\n\n' + MENSAJE_REGRESO_MENU_BAJAS
    elif text == '¿Hasta cuándo tengo para darme de baja definitiva?':
            return '¿Hasta cuándo tengo para darme de baja definitiva?\n\nDurante todo el periodo escolar. Se debe consultar las fechas de publicación y proceso a seguir en https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#baj\n\n\n' + MENSAJE_REGRESO_MENU_BAJAS
    elif text == '¿Una vez que regrese de baja temporal como podré reinscribirme?':
            return '¿Una vez que regrese de baja temporal como podré reinscribirme?\n\nDeberás solicitar tu cita con el departamento de gestión escolar de manera presencial o via Whatsapp https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#ase\nTu cita dependerá del estatus como alumno regural o irregular. NO PODRÁS SOLICITAR BAJA con materias desfasadas.\n\n\n' + MENSAJE_REGRESO_MENU_BAJAS
    #espa
    elif text == '¿En que casos debo presentar saberes previamente adquiridos?':
            return '¿En que casos debo presentar saberes previamente adquiridos?\n\nEl alumno debera estar inscrito y no haberla cursado con anterioridad.\n\n\n' + MENSAJE_REGRESO_MENU_ESPA
    elif text == '¿Cuántas veces puedo presentar un examen de saberes previamente adquiridos?':
            return '¿Cuántas veces puedo presentar un examen de saberes previamente adquiridos?\n\nPuede presentar cada unidad de aprendizaje una sola vez durante toda su trayectoria académica.\n\n\n' + MENSAJE_REGRESO_MENU_ESPA
    elif text == '¿Qué proceso debo seguir para presentar un examen de saberes previmente adquiridos?':
            return '¿Qué proceso debo seguir para presentar un examen de saberes previmente adquiridos?\n\nDeberás contar con una reinscripción y revisar la información publicada dentro de los primeros 10 días iniciado el semestre. Considera lo siguiente:\n-Tendrás que llenar tu solicitud.\n-El jefe de programa académico te hará una previa entrevista para conocer tus conocimientos de la unidad de aprendizaje.\n-En caso de no aprovar el examen de saberes previamente adquiridos, la calificación no se verá reflejada en tu kardex.\n\n\n' + MENSAJE_REGRESO_MENU_ESPA
    #carga menor
    elif text == '¿Cuándo me corresponde la carta por carga menor a la mínima?':
            return '¿Cuándo me corresponde la carta por carga menor a la mínima?\n\nSi eres alumno regular con una carga menor a la mínima de tu programa académico.\nConsulta la tabla de cargas https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#carga\n\n\n' + MENSAJE_REGRESO_MENU_MENOR
    elif text == '¿Cuándo me corresponde dictamen  por carga menor a la mínima?':
            return '¿Cuándo me corresponde dictamen  por carga menor a la mínima?\n\nSi eres alumno irregular con una carga menor a la mínima de tu programa académico\nConsulta la tabla de cargas https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#carga\n\n\n' + MENSAJE_REGRESO_MENU_MENOR
    elif text == '¿Si tengo un dictamen vigente que me permitió reinscribirme, debo de solicitar la carta o el dictamen?':
            return '¿Si tengo un dictamen vigente que me permitió reinscribirme, debo de solicitar la carta o el dictamen?\n\nNo es necesario, ya que el dictamen vigente te ampara la inscripción al semestre en curso.\n\n\n' + MENSAJE_REGRESO_MENU_MENOR
    #electivas
    elif text == '¿Cuándo procede un dictamen UPIICSA para acreditar Electivas?':
            return '¿Cuándo procede un dictamen UPIICSA para acreditar Electivas?\n\nSi dejaste pasar un semestre desde tu última inscripción y aún cuentas con periodos para cumplir la totalidad de créditos de tu programa académico.\n\n\n' + MENSAJE_REGRESO_MENU_ELECTIVAS
    elif text == '¿Cuándo procede un dictamen Zacatenco para acreditar Electivas?':
            return '¿Cuándo procede un dictamen Zacatenco para acreditar Electivas?\n\nSi dejaste pasar un semestre desde tu última inscripción y/o , ya no cuentas con periodos para cumplir la totalidad de créditos de tu programa académico.\n\n\n' + MENSAJE_REGRESO_MENU_ELECTIVAS
    elif text == '¿En cuánto tiempo se verá reflejada mi electiva en kardex?':
            return '¿En cuánto tiempo se verá reflejada mi electiva en kardex?\n\nUna vez validadas las electivas por parte de la coordinación, serán acreditadas cuando se valide que tu trayectoria académica lo permite sin necesidad de dictamen, durante las fechas previamente acordadas en los calendarios publicados.\n\n\n' + MENSAJE_REGRESO_MENU_ELECTIVAS
    #equivalencias
    elif text == '¿Cuáles son las equivalencias que pueden aplicar en mi trayectoria académica?':
            return '¿Cuáles son las equivalencias que pueden aplicar en mi trayectoria académica?\n\nSi tienes un cambio de carrera, te fuiste de movilidad académica o, vienes de otro plantel.\nTodas estas están sujetas a la revisión y autorización previa de la DAE y DES según los dictámenes, oficios y equivalencias que se emitan.\n\n\n' + MENSAJE_REGRESO_MENU_EQUIVALENCIAS
    elif text == '¿Cuánto tiempo tarda en verse reflejadas mis equivalencias?':
            return '¿Cuánto tiempo tarda en verse reflejadas mis equivalencias?\n\nUna vez que la DAE y DES determinan que, si proceden las equivalencias, envían los oficios y dictámenes para su revisión y carga, esto se verá reflejado durante el semestre en curso de la solicitud.\n\n\n' + MENSAJE_REGRESO_MENU_EQUIVALENCIAS
    elif text == '¿Cuántas equivalencias puedo tener?':
            return '¿Cuántas equivalencias puedo tener?\n\nLas que en el proceso que hayas aplicado te autoricen y tu programa y plan de estudios estén vigentes.\n\n\n' + MENSAJE_REGRESO_MENU_EQUIVALENCIAS
    

    return 'No entendi que necesitas'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str=update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type} : "{text}"')

    if message_type=='group':
        if BOT_USERNAME in text:
             new_text: str= text.replace(BOT_USERNAME,'').strip()
             response: str = handle_response(new_text)
        else:
             return
    else:
        response: str=handle_response(text)

    print ('Bot: ', response )
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
     print(f'Update {update} caused error {context.error}')

if __name__ =='__main__':
    print('Bot started')
    app=Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('reinscripcion',reinscripcion_command))
    app.add_handler(CommandHandler('tramites',tramites_command))
    app.add_handler(CommandHandler('dictamenes',dictamenes_command))
    app.add_handler(CommandHandler('ets',ets_command))
    app.add_handler(CommandHandler('inscripcion',inscripcion_command))
    app.add_handler(CommandHandler('bajadeunidades',bajaDeUnidades_command))
    app.add_handler(CommandHandler('bajas',baja_command))
    app.add_handler(CommandHandler('espa',espa_command))
    app.add_handler(CommandHandler('cargamenor',cargaMenor_command))
    app.add_handler(CommandHandler('electivas',electivas_command))
    app.add_handler(CommandHandler('equivalencias',equivalencias_command))
    app.add_handler(CommandHandler('paginage',pagina_command))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)

    app.run_polling(poll_interval=3)

