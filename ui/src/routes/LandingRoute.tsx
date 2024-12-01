import React from 'react';
import styles from './LandingRoute.module.css';

const LandingRoute: React.FC = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Welcome</h1>
    </div>
  );
};

export default LandingRoute;