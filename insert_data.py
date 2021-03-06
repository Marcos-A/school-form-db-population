# -*- coding: UTF-8 -*-
from config import config
import csv
import os
import psycopg2
import sys
from datetime import datetime
from pytz import timezone
from query_master import *


sys.path.append(os.path.dirname(__file__))
DEGREE_FILE = 'input/degree.csv'
DEPARTMENT_FILE = 'input/department.csv'
GROUP_FILE = 'input/group.csv'
LEVEL_FILE = 'input/level.csv'
QUESTION_FILE = 'input/question.csv'
SUBJECT_FILE = 'input/subject.csv'
TOPIC_FILE = 'input/topic.csv'
TRAINER_FILE = 'input/trainer.csv'
TYPE_FILE = 'input/type.csv'
    

def read_departments(input_file):
    try:
        departments = ()
        with open(input_file, 'r', encoding='utf-8') as departments_file:
            departments_reader = csv.DictReader(departments_file)

            for department in departments_reader:
                code = department['code']
                name = department['name']

                departments += ((code, name,),)

            return departments
    except Exception as e:
        catch_exception(e)


def insert_departments(departments):
    sql = """
             INSERT INTO department(code, name)
             VALUES(%s, %s);
          """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.executemany(sql, departments)
        cursor.close()
        conn.commit()
        succeed()
    except (Exception, psycopg2.DatabaseError) as error:
        catch_exception(error)
    finally:
        if conn is not None:
            conn.close()


def read_levels(input_file):
    try:
        levels = ()
        with open(input_file, 'r', encoding='utf-8') as levels_file:
            levels_reader = csv.DictReader(levels_file)

            for level in levels_reader:
                name = level['name']
                code = level['code']

                levels += ((name, code,),)

            return levels
    except Exception as e:
        catch_exception(e)


def insert_levels(levels):
    sql = """
             INSERT INTO level(name, code)
             VALUES(%s, %s);
          """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.executemany(sql, levels)
        cursor.close()
        conn.commit()
        succeed()
    except (Exception, psycopg2.DatabaseError) as error:
        catch_exception(error)
    finally:
        if conn is not None:
            conn.close()


def read_degrees(input_file):
    try:
        degrees = ()
        with open(input_file, 'r', encoding='utf-8') as degrees_file:
            degrees_reader = csv.DictReader(degrees_file)

            for degree in degrees_reader:
                code = degree['code']
                name = degree['name']
                department_id = get_department_id(degree['department_code'])
                level_id = get_level_id(degree['level_code'])

                degrees += ((code, name, department_id, level_id,),)

            return degrees
    except Exception as e:
        catch_exception(e)


def insert_degrees(degrees):
    sql = """
             INSERT INTO degree(code, name, department_id, level_id)
             VALUES(%s, %s, %s, %s);
          """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.executemany(sql, degrees)
        cursor.close()
        conn.commit()
        succeed()
    except (Exception, psycopg2.DatabaseError) as error:
        catch_exception(error)
    finally:
        if conn is not None:
            conn.close()


def read_groups(input_file):
    try:
        groups = ()
        with open(input_file, 'r', encoding='utf-8') as groups_file:
            groups_reader = csv.DictReader(groups_file)

            for group in groups_reader:
                name = group['name']
                degree_id = get_degree_id(group['degree_code'])

                groups += ((name, degree_id,),)

            return groups
    except Exception as e:
        catch_exception(e)


def insert_groups(groups):
    sql = """
             INSERT INTO "group"(name, degree_id)
             VALUES(%s, %s);
          """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.executemany(sql, groups)
        cursor.close()
        conn.commit()
        succeed()
    except (Exception, psycopg2.DatabaseError) as error:
        catch_exception(error)
    finally:
        if conn is not None:
            conn.close()


def read_topics(input_file):
    try:
        topics = ()
        with open(input_file, 'r', encoding='utf-8') as topics_file:
            topics_reader = csv.DictReader(topics_file)

            for topic in topics_reader:
                name = topic['name']

                topics += ((name,),)

            return topics
    except Exception as e:
        catch_exception(e)


def insert_topics(topics):
    sql = """
             INSERT INTO topic(name)
             VALUES(%s);
          """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.executemany(sql, topics)
        cursor.close()
        conn.commit()
        succeed()
    except (Exception, psycopg2.DatabaseError) as error:
        catch_exception(error)
    finally:
        if conn is not None:
            conn.close()


def read_types(input_file):
    try:
        types = ()
        with open(input_file, 'r', encoding='utf-8') as types_file:
            types_reader = csv.DictReader(types_file)

            for type in types_reader:
                name = type['name']

                types += ((name,),)

            return types
    except Exception as e:
        catch_exception(e)


def insert_types(types):
    sql = """
             INSERT INTO type(name)
             VALUES(%s);
          """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.executemany(sql, types)
        cursor.close()
        conn.commit()
        succeed()
    except (Exception, psycopg2.DatabaseError) as error:
        catch_exception(error)
    finally:
        if conn is not None:
            conn.close()


def read_questions(input_file):
    try:
        questions = ()
        with open(input_file, 'r', encoding='utf-8') as questions_file:
            questions_reader = csv.DictReader(questions_file)

            for question in questions_reader:
                sort = question['sort']
                statement = question['statement']
                disabled = format_timestamp(question['disabled'])
                type_id = get_type_id(question['type_name'])
                level_id = get_level_id(question['level_code'])
                topic_id = get_topic_id(question['topic_name'])
                created = format_timestamp(question['created'])

                questions += ((sort, statement, disabled, type_id, level_id, topic_id, created,),)

            return questions
    except Exception as e:
        catch_exception(e)


def insert_questions(questions):
    sql = """
             INSERT INTO question(sort, statement, disabled, type_id, level_id, topic_id, created)
             VALUES(%s, %s, %s, %s, %s, %s, %s);
          """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.executemany(sql, questions)
        cursor.close()
        conn.commit()
        succeed()
    except (Exception, psycopg2.DatabaseError) as error:
        catch_exception(error)
    finally:
        if conn is not None:
            conn.close()


def read_subjects(input_file):
    try:
        subjects = ()
        with open(input_file, 'r', encoding='utf-8') as subjects_file:
            subjects_reader = csv.DictReader(subjects_file)

            for subject in subjects_reader:
                code = subject['code']
                name = subject['name']
                degree_id = get_degree_id(subject['degree_code'])
                topic_id = get_topic_id(subject['topic_name'])

                subjects += ((code, name, degree_id, topic_id,),)

            return subjects
    except Exception as e:
        catch_exception(e)


def insert_subjects(subject):
    sql = """
             INSERT INTO subject(code, name, degree_id, topic_id)
             VALUES(%s, %s, %s, %s);
          """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.executemany(sql, subject)
        cursor.close()
        conn.commit()
        succeed()
    except (Exception, psycopg2.DatabaseError) as error:
        catch_exception(error)
    finally:
        if conn is not None:
            conn.close()


def format_timestamp(timestamp):
    # Convert empty timestamp data to null value
    if not timestamp:
        return None
    # Convert timestamp string to timestampt with timezone object
    else:
        localtz = timezone('UTC')
        timestamp_without_tz = timestamp.split('+')[0]
        datetime_format_timestamp = datetime.strptime(timestamp_without_tz, '%Y-%m-%d %H:%M:%S.%f')
        tz_aware_timestamp = localtz.localize(datetime_format_timestamp)
        return tz_aware_timestamp


if __name__ == '__main__':
    print("\u200a\u200aInserting departments data...", end=" ")
    departments = read_departments(DEPARTMENT_FILE)
    insert_departments(departments)

    print("\u200a\u200aInserting levels data...", end=" ")
    levels = read_levels(LEVEL_FILE)
    insert_levels(levels)

    print("\u200a\u200aInserting degrees data...", end=" ")
    degrees = read_degrees(DEGREE_FILE)
    insert_degrees(degrees)

    print("\u200a\u200aInserting groups data...", end=" ")
    groups = read_groups(GROUP_FILE)
    insert_groups(groups)

    print("\u200a\u200aInserting topics data...", end=" ")
    topics = read_topics(TOPIC_FILE)
    insert_topics(topics)

    print("\u200a\u200aInserting types data...", end=" ")
    types = read_types(TYPE_FILE)
    insert_types(types)

    print("\u200a\u200aInserting questions data...", end=" ")
    questions = read_questions(QUESTION_FILE)
    insert_questions(questions)

    print("\u200a\u200aInserting subjects data...", end=" ")
    subjects = read_subjects(SUBJECT_FILE)
    insert_subjects(subjects)
