from config import config
import psycopg2


def get_degree_id(degree_code):
    sql = """
            SELECT id FROM degree
            WHERE code = %s;
         """
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql, (degree_code,))
    degree_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    return degree_id


def get_department_id(department_code):
    sql = """
             SELECT id FROM department
             WHERE code = %s;
          """
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql, (department_code,))
    department_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    return department_id


def get_level_id(level_code):
    sql = """
            SELECT id FROM level
            WHERE code = %s;
         """
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql, (level_code,))
    level_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    return level_id


def get_topic_id(topic_name):
    sql = """
            SELECT id FROM topic
            WHERE name = %s;
         """
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql, (topic_name,))
    topic_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    return topic_id


def get_type_id(type_name):
    sql = """
            SELECT id FROM type
            WHERE name = %s;
         """
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql, (type_name,))
    type_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    return type_id